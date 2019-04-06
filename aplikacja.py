import matplotlib.pyplot as plt
import numpy as np
from populacja import Populacja
from matplotlib.widgets import RadioButtons, Slider, Button
import generujDane as gd


class Aplikacja:
    def __init__(self, populacja, data):

        self.flaga_krzyzowanie = 0
        self.flaga_threshold = 0
        self.data = data
        self.populacja = populacja
        self.fig, self.ax = plt.subplots()

        # Tworzenie i ustawianie elementow graficznych w aplikacji
        self.bttn_krzyzowanie =\
            RadioButtons(plt.axes([0.01, 0.7, 0.2, 0.15]),
                         labels=["usrednianie", "interpolacja"])
        self.bttn_treshold =\
            RadioButtons(plt.axes([0.01, 0.5, 0.2, 0.15]),
                         labels=["threshold_1", "threshold_2"])

        self.bttn_go = Button(plt.axes([0.1, 0.4, 0.1, 0.05]), label="GO")
        self.bttn_skip = Button(plt.axes([0.1, 0.3, 0.1, 0.05]), label="SKIP")

        axpm = plt.axes([0.25, 0.0, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        self.slider_pm =\
<<<<<<< HEAD
            Slider(axpm, 'PM', 0.0, 1.0, valinit=0.5)

        axmi = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
=======
            Slider(axpm, 'PM', 0.0, 1.0, valinit=self.populacja.pm)
        
        axmi = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')                 
>>>>>>> 6f12f73f85324f9b325a7c53a864a819f6753be9
        self.slider_mi =\
            Slider(axmi, 'MI', 10, 30, valinit=self.populacja.mi, valfmt="%i")

        axlam = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        self.slider_lam =\
<<<<<<< HEAD
            Slider(axlam, 'LAM', 30, 100, valinit=0.5, valfmt="%i")

=======
            Slider(axlam, 'LAM', 30, 100, valinit=self.populacja.lam, valfmt="%i")
        
>>>>>>> 6f12f73f85324f9b325a7c53a864a819f6753be9
        plt.subplots_adjust(bottom=0.2, left=0.26)

        self.slider_pm.on_changed(self.update_pm)
        self.slider_mi.on_changed(self.update_mi)
        self.slider_lam.on_changed(self.update_lam)
        self.bttn_krzyzowanie.on_clicked(self.rodzaj_krzyzowania)
        self.bttn_treshold.on_clicked(self.rodzaj_threshold)
        self.bttn_go.on_clicked(self.go)
        self.bttn_skip.on_clicked(self.skip)

        self.rysuj_rodzica()
        plt.show()

    # Funkcja pozwalajaca na przejscie 10 pokolen
    # za pomoca wywolania funkcji go w petli
    def skip(self, event):
        for x in range(0, 10, 1):
            self.go(event)

    # Funkcja pozwalajaca na przejscie 1 pokolenia
    def go(self, event):
        self.bttn_go.label.set_text("licze..")
        if self.flaga_krzyzowanie == 0:
            self.populacja.krzyzowanie()
        else:
            self.populacja.krzyzowanie_interpolacja()
        if self.flaga_threshold == 0:
            self.populacja.selekcja_loss_1()
        else:
            self.populacja.selekcja_loss_2()
        self.ax.cla()
        self.rysuj_rodzica()
        self.bttn_go.label.set_text("GO")

    # Funkcja zmieniajaca wartosc zmiennej flaga_threshold
    # reagujaca na wcisniecie radio buttona
    def rodzaj_threshold(self, event):
        if event == "threshold_1":
            self.flaga_threshold = 0
        else:
            self.flaga_threshold = 1

    # Funkcja zmieniajaca wartosc zmiennej flaga_krzyzowanie
    # reagujaca na wcisniecie radio buttona
    def rodzaj_krzyzowania(self, event):
        if event == "usrednianie":
            self.flaga_krzyzowanie = 0
        else:
            self.flaga_krzyzowanie = 1

    # Funkcja uaktualniajaca pm - prawdopodobienstwo mutacji
    def update_pm(self, val):
        self.populacja.pm = val

    # Funkcja uaktualniajaca mi - wielkosc populacji
    def update_mi(self, val):
        self.populacja.mi = int(val)

    # Funkcja uaktualniajaca lam - lambda, ilosc potomkow
    def update_lam(self, val):
        self.populacja.lam = int(val)

    # Funkcja rysujaca rodzicow
    def rysuj_rodzica(self):

        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)

        x = np.linspace(-2, 2, 20)

        for os in self.populacja.populacja_P:
            wsp_a = -os.wektor_wspol_w[1]/os.wektor_wspol_w[2]
            wsp_b = -os.wektor_wspol_w[0]/os.wektor_wspol_w[2]
            self.ax.plot(x, wsp_a*x+wsp_b, '-r')

        x = np.linspace(-2, 2, 10)

<<<<<<< HEAD
=======
        for os in self.populacja.populacja_potomkow:
            wsp_a = -os.wektor_wspol_w[1]/os.wektor_wspol_w[2]
            wsp_b = -os.wektor_wspol_w[0]/os.wektor_wspol_w[2]
            self.ax.plot(x, wsp_a*x+wsp_b, '-y', alpha=0.4)
>>>>>>> 6f12f73f85324f9b325a7c53a864a819f6753be9
        for x in self.data:
            if x[2] == 0.:
                self.ax.scatter(x[0], x[1], s=10, c="green")
            else:
                self.ax.scatter(x[0], x[1], s=10, c="blue")


<<<<<<< HEAD
def generuj_dane():
    # Kazda z grup dzielimy na 3 cwiartki:
    # a1(I), a2(II), a3(IV)
    # b1(III), b2(II), b3(IV)
    # i losujemy dla kazdej cwiartki punkty
<<<<<<< HEAD
    a1 = 2*(np.random.rand(200, 2))
    a2 = 2*(np.random.rand(200, 2))
    a3 = 2*(np.random.rand(200, 2))
    b1 = -2*(np.random.rand(200, 2))
    b2 = -2*(np.random.rand(200, 2))
    b3 = -2*(np.random.rand(200, 2))
    a1 = 2*(np.random.rand(200, 2))
    a2 = 2*(np.random.rand(200, 2))
    a3 = 2*(np.random.rand(200, 2))
    b1 = -2*(np.random.rand(200, 2))
    b2 = -2*(np.random.rand(200, 2))
    b3 = -2*(np.random.rand(200, 2))
=======

    a1 = 2*(np.random.rand(200,2))
    a2 = 2*(np.random.rand(200,2))
    a3 = 2*(np.random.rand(200,2))
    b1 = -2*(np.random.rand(200,2))
    b2 = -2*(np.random.rand(200,2))
    b3 = -2*(np.random.rand(200,2))
>>>>>>> 6f12f73f85324f9b325a7c53a864a819f6753be9

    # Zamiana wspolrzednych tak, aby punkty
    # z danego obszaru znajdowaly sie w
    # odpowiedniej cwiartce
    for x in a2[:]:
        x[1] = x[1]*(-1)

    for x in a3[:]:
        x[0] = x[0]*(-1)

    for x in b2[:]:
        x[1] = x[1]*(-1)

    for x in b3[:]:
        x[0] = x[0]*(-1)

    # Za pomoca funkcji y = -0.5*x oraz y=2*x
    # ograniczamy zbior punktow poprzez dodanie
    # spelniajacych zalozenia do nowej tabeli bis
    a2bis = []
    for x in a2:
        if(x[1] >= (-0.5 * x[0])):
            a2bis.append(x)

    a3bis = []
    for x in a3:
        if(x[1] >= (-2 * x[0])):
            a3bis.append(x)

    b2bis = []
    for x in b2:
        if(x[1] < (-0.5 * x[0])):
            b2bis.append(x)

    b3bis = []
    for x in b3:
        if(x[1] < (-2 * x[0])):
            b3bis.append(x)

    # Sklejamy a1, a2bis i a3bis
    for i in range(0, len(a2bis), 1):
        a1 = np.vstack([a1, a2bis[i]])
    for i in range(0, len(a3bis), 1):
        a1 = np.vstack([a1, a3bis[i]])

    a1 = np.append(a1, np.ones((len(a1), 1)), axis=1)

    # Sklejamy b1, b2bis i b3bis
    for i in range(0, len(b2bis), 1):
        b1 = np.vstack([b1, b2bis[i]])
    for i in range(0, len(b3bis), 1):
        b1 = np.vstack([b1, b3bis[i]])

    b1 = np.append(b1, np.zeros((len(b1), 1)), axis=1)

    # Zwracamy wynik w postaci zlaczenia a1 z b1
    return np.vstack([a1, b1])

<<<<<<< HEAD
=======
>>>>>>> 395319674f035c776f33581f261e43dddca4091b
if __name__ == "__main__":
    B = gd.generuj_dane()
    app = Aplikacja(Populacja(30, 10, 0.2, B), B)
=======
    app = Aplikacja(Populacja(40, 18, 0.2, B), B)
>>>>>>> 6f12f73f85324f9b325a7c53a864a819f6753be9
