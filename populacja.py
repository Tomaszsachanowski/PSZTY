"""
author:
    Tomasz Sachanowski,
    Aleksander Krzemiński

"""
from osobnik import Osobnik
import numpy as np
from random import sample
from random import random


class Populacja:

    def __init__(self, lam, mi, pm, data=None):
        """
        lam- liczba generowanych potomkow
        mi- liczba osobnikow w każdym pokoleniu
        pm - prawdopodobienstwo mutacji
        """
        self.data = data
        self.wymiar_d = data.shape[1]
        self.lam = lam
        self.mi = mi
        # pm trzeba podac jako 0.*
        self.pm = pm

        self.populacja_P = [
            Osobnik(wektor_wspol_w=wektor, data=data)
            for wektor in ((np.random.rand(mi, self.wymiar_d)-0.5)*4)]

        self.populacja_potomkow = []

    def krzyzowanie_interpolacja(self):
        # czyszcze liste aby tworzyc nowych potomkow
        self.populacja_potomkow.clear()
        # w petli bo mam zrobic lam potomkow
        for i in range(0, self.lam, 1):
            # losuje dwóch rodziców bez powtórzeń ale ze zwracaniem
            rodzic_A, rodzic_B = sample(population=self.populacja_P, k=2)
            a = np.random.rand(1)
            wektor_interpolacji = a*rodzic_A.wektor_wspol_w + (1-a)*rodzic_B.wektor_wspol_w
            # mutacja
            nowy_wektor = self.mutacja(wektor_interpolacji)
            # tworze nowego osobnika
            potomek = Osobnik(wektor_wspol_w=nowy_wektor, data=self.data)
            self.populacja_potomkow.append(potomek)

    def krzyzowanie(self):
        # czyszcze liste aby tworzyc nowych potomkow
        self.populacja_potomkow.clear()
        # w petli bo mam zrobic lam potomkow
        for i in range(0, self.lam, 1):
            # losuje dwóch rodziców bez powtórzeń ale ze zwracaniem
            rodzic_A, rodzic_B = sample(population=self.populacja_P, k=2)
            wektor_sumy = (rodzic_A.wektor_wspol_w + rodzic_B.wektor_wspol_w)
            wektor_sr_arytm = wektor_sumy/2
            # mutacja
            nowy_wektor = self.mutacja(wektor_sr_arytm)
            # tworze nowego osobnika
            potomek = Osobnik(wektor_wspol_w=nowy_wektor, data=self.data)
            self.populacja_potomkow.append(potomek)

    # Ta funkcja musi byc uruchamiana przez krzyzowanie dla kazdego nowego potomka
    def mutacja(self, wektor_wspol):
        if random() < self.pm:
            # tworze wektor o takiej samej wielkosci jak wektor wspolczynnikow
            # i umieszczam w nim wylosowane prawdopodobienstwa
            wektor_mutacji = np.random.normal(loc=1.0, scale=0.3, size=wektor_wspol.shape[0])
            wektor_wspol = wektor_wspol*wektor_mutacji
        return wektor_wspol

    def selekcja_loss_1(self):
        tmp = self.populacja_P + self.populacja_potomkow
        tmp.sort(key=lambda osobnik: osobnik.wartosc_loss_1)
        self.populacja_P = tmp[:self.mi]

    def selekcja_loss_2(self):
        tmp = self.populacja_P + self.populacja_potomkow
        tmp.sort(key=lambda osobnik: osobnik.wartosc_loss_2)
        self.populacja_P = tmp[:self.mi]
