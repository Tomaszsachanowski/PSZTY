import matplotlib.pyplot as plt
import numpy as np
from populacja import Populacja
from matplotlib.widgets import RadioButtons, Slider

class Aplikacja:
    def __init__(self, populacja):
        self.populacja = populacja
        self.fig, self.ax = plt.subplots()
        self.bttn_krzyzowanie =\
            RadioButtons(plt.axes([0.01, 0.7, 0.2, 0.15]),
                         labels=["usrednianie", "wagowe"])

        #plt.subplots_adjust(hspace=10.5)
        axpm = plt.axes([0.25, 0.0, 0.65, 0.03], facecolor='lightgoldenrodyellow')                 
        self.slider_pm =\
            Slider(axpm, 'PM', 0.0, 1.0, valinit=0.5)
        
        axmi = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')                 
        self.slider_mi =\
            Slider(axmi, 'MI', 10, 30, valinit=0.5, valfmt="%i")

        axlam = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')                 
        self.slider_lam =\
            Slider(axlam, 'LAM', 30, 100, valinit=0.5, valfmt="%i")
        
        plt.subplots_adjust(bottom=0.2, left=0.26)

        def update_pm(val):
            self.populacja.pm = val
            print('Pm = ', val)

        def update_mi(val):
            self.populacja.mi = val
            print('Mi = ', val)

        def update_lam(val):
            self.populacja.lam = val
            print('Lam = ', val)

        self.slider_pm.on_changed(update_pm)
        self.slider_mi.on_changed(update_mi)
        self.slider_lam.on_changed(update_lam)

        plt.show()

if __name__ == "__main__":

    # Kazda z grup dzielimy na 3 cwiartki:
    # a1(I), a2(II), a3(IV)
    # b1(III), b2(II), b3(IV)
    # i losujemy dla kazdej cwiartki punkty

    a1 = 2*(np.random.rand(200, 2))
    a2 = 2*(np.random.rand(200, 2))
    a3 = 2*(np.random.rand(200, 2))
    b1 = -2*(np.random.rand(200, 2))
    b2 = -2*(np.random.rand(200, 2))
    b3 = -2*(np.random.rand(200, 2))

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

    app = Aplikacja(Populacja(30, 10, 0.2, B))