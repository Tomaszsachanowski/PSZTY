"""
autor Tomasz Sachanowski
"""
import numpy as np


class Perceptron:
    """
    klasa reprezentująca pojedynczy neuron
    w naszej sieci(perceptron)
    Perceptron prosty jest najprostszą SSN,
    używaną do klasyfikacjibinarnej.

    mi - współczynik uczneia się

    wymiar_d - wymiar wektora Xj
    """
    def __init__(self, mi, wymiar_d):
        # jak wielki wektor potrzebujemy
        # +1 bo jeszce W0
        self.wymiar_wektora_w = wymiar_d + 1
        # współczynik uczenia się (0,1>
        self.mi = mi
        # losowe współczynik w z przedziału (-1, 1)
        self.wektor_wspol_w = (np.random.rand(self.wymiar_wektora_w)-0.5)*2
        self.wartosc_funkcji_aktywacji = None

    def Threshold_1(self, wektor_x):
        """
        funkcja aktywacji
        Threshold(y) = 1 jeśli y >= 0 i 0 wpp.
        """
        wektor_tmp = np.ones(self.wymiar_wektora_w, dtype='int')
        wektor_tmp[1:] = wektor_x
        # to wyzej jest po to by miec [1, x1, x2, x3, xn]
        # pomaga przy iloczynie xj*w - iloczyn sklarny
        # bo wtedy mam 1*w0+ x1*w1 + xn*wn
        iloczyn_sklarny_xj_w = np.dot(wektor_tmp, self.wektor_wspol_w)

        if iloczyn_sklarny_xj_w > 0:
            self.wartosc_funkcji_aktywacji = 1
        else:
            self.wartosc_funkcji_aktywacji = 0

    def uczenie(self, wektor_x, klasa_y):
        """
        klasa_y - zmienna xd do jakiej grupy nalezy dany wektor
        """
        self.Threshold_1(wektor_x)
        e = klasa_y - self.wartosc_funkcji_aktywacji
        if e == 1:
            self.aktualizacja_współczynikow_dodatnia(wektor_x)
        elif e == -1:
            self.aktualizacja_współczynikow_ujemna(wektor_x)

    def aktualizacja_współczynikow_dodatnia(self, wektor_x):
        wektor_tmp = np.ones(self.wymiar_wektora_w, dtype='int')
        wektor_tmp[1:] = wektor_x
        # to wyzej jest po to by miec [1, x1, x2, x3, xn]
        self.wektor_wspol_w += self.mi*wektor_tmp

    def aktualizacja_współczynikow_ujemna(self, wektor_x):
        wektor_tmp = np.ones(self.wymiar_wektora_w, dtype='int')
        wektor_tmp[1:] = wektor_x
        # to wyzej jest po to by miec [1, x1, x2, x3, xn]
        self.wektor_wspol_w -= self.mi*wektor_tmp