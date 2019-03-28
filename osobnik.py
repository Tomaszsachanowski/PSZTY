"""
author:
    Tomasz Sachanowski,
    Aleksander Krzemiński

"""
import numpy as np


class Osobnik:

    def __init__(self, wektor_wspol_w, data):

        self.wektor_wspol_w = wektor_wspol_w
        self.data = data

        self.wartosc_loss_1 = self.wartosc_loss(param=1)
        self.wartosc_loss_2 = self.wartosc_loss(param=2)

    def __Threshold_1(self, wektor_x):
        """
        funkcja aktywacji
        Threshold(y) = 1 jeśli y >= 0 i 0 wpp.
        """
        wektor_tmp = np.ones(wektor_x.shape[0])
        wektor_tmp[1:] = wektor_x[:-1]
        # to wyzej jest po to by miec [1, x1, x2, x3, xn]
        # pomaga przy iloczynie xj*w - iloczyn sklarny
        # bo wtedy mam 1*w0+ x1*w1 + xn*wn
        # wektor_x.shape[0] podaje jak dlugi jest wektor [x1,x2,.., xd]
        # jest [:-1] bo ostatni to xd
        iloczyn_sklarny_xj_w = np.dot(wektor_tmp, self.wektor_wspol_w)
        if iloczyn_sklarny_xj_w > 0:
            return 1
        else:
            return 0

    def __Threshold_2(self, wektor_x):
        """
        funkcja sigmoidalana
        Threshold(y) = 1/(1+e^(-x))
        """
        wektor_tmp = np.ones(wektor_x.shape[0])
        wektor_tmp[1:] = wektor_x[:-1]
        # to wyzej jest po to by miec [1, x1, x2, x3, xn]
        # pomaga przy iloczynie xj*w - iloczyn sklarny
        # bo wtedy mam 1*w0+ x1*w1 + xn*wn
        # wektor_x.shape[0] podaje jak dlugi jest wektor [x1,x2,.., xd]
        # jest [:-1] bo ostatni to xd i jego nie liczymy do wektora
        iloczyn_sklarny_xj_w = np.dot(wektor_tmp, self.wektor_wspol_w)
        sigmoida = 1/(1+np.exp(-iloczyn_sklarny_xj_w))

        return sigmoida

    def wartosc_loss(self, param):
        tmp = 0
        for wektor_xi in self.data:
            if param == 1:
                treshold = self.__Threshold_1(wektor_xi)
            else:
                treshold = self.__Threshold_2(wektor_xi)

            roznica_bledu = wektor_xi[-1] - treshold
            tmp += roznica_bledu**2
        return tmp
