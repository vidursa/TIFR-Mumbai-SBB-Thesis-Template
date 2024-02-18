@ECHO OFF
makeindex  main.idx
makeindex -s main.ist -t main.alg -o main.acr main.acn
makeindex -s main.ist -o main.gls main.glo
