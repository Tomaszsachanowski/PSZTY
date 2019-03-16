# PSZTY
TM.AE.2. Niech D będzie danym zbiorem N d-wymiarowych wektorów xj liczb
rzeczywistych, w którym xd  {0, 1}, natomiast h : R

d  R funkcją h(x) = Threshold(w0 +

i=1,...,d-1 wi

*xi). Zaprojektować i zaimplementować algorytm ewolucyjny, który będzie

minimalizował wartość funkcji Loss(h) = N (xd – h(xj))2

względem współczynników w.
Implementacja powinna umożliwiać wybór spośród dwóch definicji funkcji Threshold: 1)
Threshold(y) = 1 jeśli y >= 0 i 0 wpp., 2) Threshold(y) = 1/(1 – e–y

). Działanie algorytmu
należy zaprezentować w formie prostej aplikacji umożliwiającej zobrazowanie kolejnych
kroków jego działania dla zbioru punktów umiejscowionych ręcznie na płaszczyźnie.

Ponadto aplikacja powinna umożliwiać wczytanie dowolnego zbioru wektorów d-
wymiarowych, wyznaczenie dla niego współczynników w zgodnie z powyższą procedurą,

a następnie odczytanie wartości funkcji h dla zadanych wektorów: w tym celu należy
przetestować działanie programu dla zbioru danych zawartych pod adresem:
https://archive.ics.uci.edu/ml/datasets/Planning+Relax. (UWAGA: Przed wczytaniem
danych do programu należy dokonać przekształcenia ostatniej współrzędnej ze zbioru {1,
2} do {0, 1}.) Aplikacja powinna także umożliwiać ustawianie innych parametrów stricte
związanych z algorytmem ewolucyjnym (takich jak: wielkość populacji,
prawdopodobieństwo mutacji, jej maksymalna siła, itp.). W dokumentacji należy
przedstawić swoje przemyślenia nad możliwością wykorzystania powyższego podejścia
do problemu klasyfikacji binarnej.