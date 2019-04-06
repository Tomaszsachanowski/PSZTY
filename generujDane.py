"""
autorzy:
    Aleksander Krzemiński,
    Tomasz Sachanowski
"""

import numpy as np

"""

Funkcja generująca nam zestaw danych testowych:

-> dwie grupy punktow - jedna w cwiartce I, druga w cwiartce III
-> dodatkowo punkty z obu grup wchodzace do cwiartki II i IV

"""


def generuj_dane():
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
