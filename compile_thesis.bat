@ECHO OFF
setlocal enabledelayedexpansion
pdflatex --shell-escape main.tex
makeindex  main.idx
makeindex -s main.ist -t main.alg -o main.acr main.acn
for %%f in (chapters\*.aux) do ( 
bibtex %%f
 )
for %%f in (appendix\*.aux) do ( 
bibtex %%f
 )
pdflatex --shell-escape main.tex
pdflatex --shell-escape main.tex