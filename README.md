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
1. The macro to generate folder structures takes a lot of memory. If compilation of the thesis halts due to lack of memory, or because --shell-escape is missing, you can either use --shell-escape or --extra-mem-bot=10000000 as suggested in this stackexchange post (https://tex.stackexchange.com/questions/7953/how-to-expand-texs-main-memory-size-pgfplots-memory-overload). If compiling from a latex editor such as TeXstudio, change these parameters from Options > Configure TeXStudio > Commands > pdflatex. The final command should look like "pdflatex.exe -synctex=1 -interaction=nonstopmode -shell-escape --extra-mem-bot=10000000 %.tex".

2. If the glossary/acronym list isn't displayed the first time the thesis is compiled, run the Make_glossary.bat file once. The second compilation should automatically include the glossary.

3. If the references are not included, your TeXstudio setup is probably not using biber as a backend. You can change this in Options > Configure TeXStudio > Build > Default Bibliography Tool.

4. I have removed support for adding figures with their legend automatically shifted to the next page due to the hassle of installing it yourself. If needed, fltpages.sty(https://www.ctan.org/pkg/fltpage) and installation of these libraries (https://en.wikibooks.org/wiki/LaTeX/Installing_Extra_Packages) are needed to invoke FPtable and FPfigure.

5. I have removed support for adding codes to the thesis since it involves a bit more headwork to get it running. In case its need, uncomment the lines following "Uncomment if codes are added in the thesis appendix" in main.tex and uncomment "\include{appendix/appendix5}" for an example of it working. Follow (https://superuser.com/questions/816340/minted-cannot-find-pygmentize-in-texstudio-on-windows-7) to get pygmentize working.


Note: I have disabled including separate references for each chapter since it is redundant and not required as per SBB guidelines. However, some reviewers are known to ask for it. You may need the `natbib` and `chapterbib` packages as used in (https://github.com/rohitsuratekar/ncbs-tifr-thesis-template).

