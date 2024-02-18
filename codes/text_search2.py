import urllib2
import openpyxl
import re
import time

_number = 94  # row start for gene list

wb = openpyxl.load_workbook("E:/E3example_copy.xlsx")


def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


for sheet in wb.worksheets[:1]:

    while True:

        while True:
            try:
                _fosmid = sheet["B" + str(_number)].value
                print(_fosmid)
                if _fosmid == None:
                    print("name exhausted")
                    wb.save("E:/E3example_copy.xlsx")
                    exit(1)
                _url1 = "http://www.wormbase.org/search/gene/" + str(_fosmid)
                f = urllib2.urlopen(_url1)
                res = f.geturl()
                if "WBGene" in res:
                    pos = res.find("WBGene")
                    _WB_ID = res[pos : pos + 14]

                    _url = (
                        "http://www.wormbase.org/rest/widget/gene/"
                        + str(_WB_ID)
                        + "/overview"
                    )

                    print(_url)

                    _scrape_gene = "<i>"
                    _scrapeend_gene = "</i>"
                    _scrape_desc = 'class="gene-link">'
                    _scrapeend_desc = '<div class="toggle ">'
                    _scrapeend_desc2 = '<div id="evidence_Provisional_description"'
                    if _scrapeend_desc > _scrapeend_desc2:
                        _scrapeend_desc = _scrapeend_desc2
                    f2 = urllib2.urlopen(_url)
                    content = f2.read()

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
                    _scrape_gene = '<span class="locus">'
                    _scrapeend_gene = '[<a href="/tools/'
                    _scrape_desc = 'class="gene-link">'
                    _scrapeend_desc = '<span id="fade">'
                    wb.save("E:/E3example_copy.xlsx")

                if _WB_ID == "":
                    print("no WB_ID found")
                    break
                _url3 = (
                    "http://www.wormbase.org/rest/widget/gene/"
                    + str(_WB_ID)
                    + "/location"
                )

                _scrape_location = '<div class="field-content">'
                _scrapeend_location = '<span title="The genomic location'

                pos = content.find(_scrape_gene)
                end_pos = content.find(_scrapeend_gene)

                pos2 = content.find(_scrape_desc)
                end_pos2 = content.find(_scrapeend_desc)
                f3 = urllib2.urlopen(_url3)
                content3 = f3.read()
                pos3 = content3.find(_scrape_location)
                end_pos3 = content3.find(_scrapeend_location)
                f3 = urllib2.urlopen(_url3)
                content3 = f3.read()

                print(cleanhtml(content[pos:end_pos]))
                sheet["H" + str(_number)] = cleanhtml(content3[pos3:end_pos3])
                sheet["I" + str(_number)] = cleanhtml(content[pos:end_pos])
                sheet["J" + str(_number)] = cleanhtml(content[pos2 + 18 : end_pos2])

            except:
                wb.save("E:/E3example_copy2.xlsx")
                print(5)
                if _fosmid == None:
                    print("finish")
                    exit(1)

                break

            _number = _number + 1
            time.sleep(10)
            print("2.")

        _number = _number + 1
        print("3.")
