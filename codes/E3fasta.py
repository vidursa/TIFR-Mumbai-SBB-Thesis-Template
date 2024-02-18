import urllib2
import openpyxl
import re
import time

_number = 1  # row start for gene list

wb = openpyxl.load_workbook("D:/example_copy11.xlsx")


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def find_instance(text):
    transcripts = set([])
    for instance in re.finditer("/rest/widget/transcript/", text):
        transcript = text[instance.end() : text.find("/", instance.end() + 7)]
        transcripts.add(transcript)
    return transcripts


for sheet in wb.worksheets[7:]:

    while True:

        while True:
            try:
                _fosmid = sheet["I" + str(_number)].value
                print(_fosmid)
                if _fosmid == None:
                    print("name exhausted")
                    wb.save("D:/example_copy12.xlsx")
                    exit(1)
                _url1 = "http://www.wormbase.org/search/gene/" + str(_fosmid)

                f = urllib2.urlopen(_url1)
                res = f.geturl()
                if "WBGene" in res:
                    pos = res.find("WBGene")
                    _WB_ID = res[pos : pos + 14]

                else:
                    _url1 = (
                        "http://www.wormbase.org/search/gene/"
                        + str(_fosmid)
                        + "/1?inline=1"
                    )

                    print(_url1)
                    f = urllib2.urlopen(_url1)
                    content = f.read()
                    pos = content.find("WBGene")
                    _WB_ID = content[pos : pos + 14]
                    if _WB_ID == "":
                        _url1 = (
                            "http://www.wormbase.org/search/gene/"
                            + str(_fosmid[:-1])
                            + "/1?inline=1"
                        )

                        print(_url1)
                        f = urllib2.urlopen(_url1)
                        content = f.read()
                        pos = content.find("WBGene")
                        _WB_ID = content[pos : pos + 14]

                if _WB_ID == "":
                    print("pseudogene")
                    sheet["H" + str(_number)] = "pseudogene"
                    break
                else:
                    sheet["H" + str(_number)] = _WB_ID

                _url = (
                    "http://www.wormbase.org/rest/widget/gene/"
                    + str(_WB_ID)
                    + "/sequences"
                )

                f2 = urllib2.urlopen(_url)
                content = f2.read()
                isoforms = find_instance(content)

                for isoform in isoforms:
                    _sequence_file = ""
                    _url2 = (
                        "http://www.wormbase.org/rest/widget/transcript/"
                        + str(isoform)
                        + "/sequences"
                    )

                    f3 = urllib2.urlopen(_url2)
                    content2 = f3.read()

                    _sequence = " spliced"
                    _sequenceend = "</div>"
                    pos = content2.find(_sequence)
                    end_pos = content2.find(_sequenceend, pos + 1)
                    _sequence_file = (
                        ">"
                        + isoform
                        + " \r\n"
                        + str(content2[pos + 14 : end_pos].strip())
                    )

                    f = open("D:/E3 sequences/" + isoform + ".txt", "wb")
                    f.write("%s" % _sequence_file)
                    f.close()

            except:
                wb.save("D:/example_copy12.xlsx")
                if _fosmid == None:
                    print("finish")
                    exit(1)

                break

            _number = _number + 1
            time.sleep(10)
            print("2")
            wb.save("D:/example_copy12.xlsx")

        _number = _number + 1
        print("3")
