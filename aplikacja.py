import matplotlib.pyplot as plt
import numpy as np
from populacja import Populacja
from matplotlib.widgets import RadioButtons, Slider, Button

class Aplikacja:
    def __init__(self, populacja, data):

        self.flaga_krzyzowanie = 0
        self.flaga_threshold = 0
        self.data = data
        self.populacja = populacja
        self.fig, self.ax = plt.subplots()
       

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
            Slider(axpm, 'PM', 0.0, 1.0, valinit=self.populacja.pm)
        
        axmi = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')                 
        self.slider_mi =\
            Slider(axmi, 'MI', 10, 30, valinit=self.populacja.mi, valfmt="%i")

        axlam = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')                 
        self.slider_lam =\
            Slider(axlam, 'LAM', 30, 100, valinit=self.populacja.lam, valfmt="%i")
        
        plt.subplots_adjust(bottom=0.2, left=0.26)

        self.slider_pm.on_changed(self.update_pm)
        self.slider_mi.on_changed(self.update_mi)
        self.slider_lam.on_changed(self.update_lam)
        self.bttn_krzyzowanie.on_clicked(self.rodzaj_krzyzowania)
        self.bttn_treshold.on_clicked(self.rodzaj_threshold)
        self.bttn_go.on_clicked(self.go)
        self.bttn_skip.on_clicked(self.skip)

        self.draw_parent()
        plt.show()
    def skip(self, event):
        for x in range(0, 10, 1):
            self.go(event)

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
        self.draw_parent()
        self.bttn_go.label.set_text("GO")

    def rodzaj_threshold(self, event):
        if event == "threshold_1":
            self.flaga_threshold = 0
        else:
            self.flaga_threshold = 1
    def rodzaj_krzyzowania(self, event):
        if event == "usrednianie":
            self.flaga_krzyzowanie = 0
        else:
            self.flaga_krzyzowanie = 1

    def update_pm(self, val):
        self.populacja.pm = val
        print('Pm = ', val)

    def update_mi(self, val):
        self.populacja.mi = int(val)
        print('Mi = ', val)

    def update_lam(self, val):
        self.populacja.lam = int(val)
        print('Lam = ', val)


    def draw_parent(self):

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

        for os in self.populacja.populacja_potomkow:
            wsp_a = -os.wektor_wspol_w[1]/os.wektor_wspol_w[2]
            wsp_b = -os.wektor_wspol_w[0]/os.wektor_wspol_w[2]
            self.ax.plot(x, wsp_a*x+wsp_b, '-y', alpha=0.4)
        for x in self.data:
            if x[2] == 0.:
                self.ax.scatter(x[0], x[1], s=10, c="green")
            else:
                self.ax.scatter(x[0], x[1], s=10, c="blue")


if __name__ == "__main__":

    # Kazda z grup dzielimy na 3 cwiartki:
    # a1(I), a2(II), a3(IV)
    # b1(III), b2(II), b3(IV)
    # i losujemy dla kazdej cwiartki punkty

    a1 = 2*(np.random.rand(200,2))
    a2 = 2*(np.random.rand(200,2))
    a3 = 2*(np.random.rand(200,2))
    b1 = -2*(np.random.rand(200,2))
    b2 = -2*(np.random.rand(200,2))
    b3 = -2*(np.random.rand(200,2))

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
        if(x[1]>=(-0.5 * x[0])):
            a2bis.append(x)

    a3bis = []
    for x in a3:
        if(x[1]>=(-2 * x[0])):
            a3bis.append(x)   
            
    b2bis = []
    for x in b2:
        if(x[1]<(-0.5 * x[0])):
            b2bis.append(x)

    b3bis = []
    for x in b3:
        if(x[1]<(-2 * x[0])):
            b3bis.append(x)

    # 
    for i in range(0,len(a2bis),1):
        a1 = np.vstack([a1, a2bis[i]])
    for i in range(0,len(a3bis),1):
        a1 = np.vstack([a1, a3bis[i]])

    a1 = np.append(a1, np.ones((len(a1), 1)), axis=1)
    a1

    for i in range(0,len(b2bis),1):
        b1 = np.vstack([b1, b2bis[i]])
    for i in range(0,len(b3bis),1):
        b1 = np.vstack([b1, b3bis[i]])

    b1 = np.append(b1, np.zeros((len(b1), 1)), axis=1)

    B = np.vstack([a1,b1])


    app = Aplikacja(Populacja(40, 18, 0.2, B), B)
