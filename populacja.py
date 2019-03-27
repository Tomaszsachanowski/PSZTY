"""
author:
    Tomasz Sachanowski,
    Aleksander Krzemiński

"""
from osobnik import Osobnik
import numpy as np
from random import sample


class Populacja:

    def __init__(self, lam, mi, data=None):
        """
        lam- liczba generowanych potomkow
        mi- liczba osobnikow w każdym pokoleniu
        """
        self.data = data
        self.wymiar_d = data.shape[1]
        self.lam = lam
        self.mi = mi

        self.populacja_P = [
            Osobnik(wektor_wspol_w=wektor, data=data)
            for wektor in ((np.random.rand(mi, self.wymiar_d)-0.5)*4)]

        self.populacja_potomkow = []

    def krzyzowanie(self):
        # czyszcze liste aby tworzyc nowych potomkow
        self.populacja_potomkow.clear()
        # w petli bo mam zrobic lam potomkow
        for i in range(0, self.lam, 1):
            # losuje dwóch rodziców bez powtórzeń ale ze zwracaniem
            rodzic_A, rodzic_B = sample(population=self.populacja_P, k=2)
            wektor_sumy = (rodzic_A.wektor_wspol_w + rodzic_B.wektor_wspol_w)
            wektor_sr_arytm = wektor_sumy/2
            # tworze nowego osobnika
            potomek = Osobnik(wektor_wspol_w=wektor_sr_arytm, data=self.data)
            self.populacja_potomkow.append(potomek)

    def selekcja_loss_1(self):
        tmp = self.populacja_P + self.populacja_potomkow
        tmp.sort(key=lambda osobnik: osobnik.wartosc_loss_1)
        self.populacja_P = tmp[:self.mi]
