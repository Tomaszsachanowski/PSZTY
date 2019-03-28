import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

class Aplikacja:
    def __init__(self):
        
        self.fig, self.ax = plt.subplots()
        self.bttn_krzyzowanie =\
            RadioButtons(plt.axes([0.05, 0.4, 0.1, 0.15]),
                         labels=["usrednianie", "wagowe"])

        plt.show()
