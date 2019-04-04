import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import numpy as np
from populacja import Populacja

class Aplikacja:
    def __init__(self, populacja, data):
    
        self.data = data
        self.populacja = populacja
        self.fig, self.ax = plt.subplots()
        self.bttn_krzyzowanie =\
            RadioButtons(plt.axes([0.05, 0.4, 0.1, 0.15]),
                         labels=["usrednianie", "wagowe"])

        self.draw_parent()
        plt.show()

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

        for x in self.data:
            if x[2] == 0.:
                self.ax.scatter(x[0], x[1], s=10, c="green")
            else:
                self.ax.scatter(x[0], x[1], s=10, c="blue")

if __name__ == "__main__":


    """

    Funkcja generująca nam zestaw danych testowych:

    -> dwie grupy punktow - jedna w cwiartce I, druga w cwiartce III
    -> dodatkowo punkty z obu grup wchodzace do cwiartki II i IV

    """

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
    populacja = Populacja(30, 10, 0.2, B)
    
    Aplikacja(populacja, B)