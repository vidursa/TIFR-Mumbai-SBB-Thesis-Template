# TIFR-Mumbai-SBB-Thesis-Template

A fork of Rohit Suratekar's thesis template (https://github.com/rohitsuratekar/ncbs-tifr-thesis-template) modified to adhere to TIFR Subject Board Biology guidelines.

# Structure

* `main.tex` : Standalone file which will combine all aspects of the thesis. You can customize view and arrangement of thesis from this file
* `Thesis.bib` : All bibliography (Automatically generated from Zotero using the BetterBibtex plugin (https://retorque.re/zotero-better-bibtex/).) 
* `front_matter\` : Includes all front matter files like declarations, certificate etc. 
* `chapters\` : Includes all chapters. To organize better, keep separate document for each chapter. Chapter 2 is Material and Methods. 
* `figs\` : All figures
* `helpers\` : Acronyms and bibliography helper file
* `appendix\` : Appendices 
* `script.bat` : Compilation script (for Windows)

# Compilation
To compile all the structures (with `pdflatex`), follow following procedure

    Note: Initial compilation might take long time if you do not have all the latex packages needed to compile. Before compiling check if you have all the packages installed. You can switch on automatic package installation if using MikTex. 

## Windows 
Just run `compile_thesis.bat` (double click it)

Alternatively, one can compile using TeXstudio as well. 

## Known bugs
1. The macro to generate folder structures takes a lot of memory. If compilation of the thesis halts due to lack of memory, you can either use -shell-escape or --extra-mem-bot=10000000 as suggested in this stackexchange post (https://tex.stackexchange.com/questions/7953/how-to-expand-texs-main-memory-size-pgfplots-memory-overload). If compiling from a latex editor such as TeXstudio, change these parameters from Options > Configure TeXStudio > Commands > pdflatex.

2. If the glossary/acronym list isn't displayed the first time the thesis is compiled, run the Make_glossary.bat file once. The second compilation should automatically include the glossary.

3. The reference seem to be duplicated for now. I didn't get time to troubleshoot it yet, but as a hack, once the thesis is compiled, you can delete the duplicated references from the .bbl file directly

Note: I have disabled including separate references for each chapter since it is redundant and not required as per SBB guidelines. However, some reviewers are known to ask for it. You may need the `natbib` and `chapterbib` packages as used in (https://github.com/rohitsuratekar/ncbs-tifr-thesis-template).
