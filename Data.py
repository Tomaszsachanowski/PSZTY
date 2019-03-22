import numpy as np

### Data class ###
# usage: printing 
# and loading data
#  from text file 
class Data:
    def __init__(self, filename):
        self.filename = filename
        self.matrix = self.loadToMatrix()
    
    # load() function -> loads data from txt file 
    def loadToMatrix(self):
       with open(self.filename, "r") as file:
        return np.loadtxt(file, delimiter=',')

    # split() function -> creates tupla out of matrix columns
    def split(self):
        mdimm = self.matrix.shape[1]
        #hpslit - horizontal split
        tupla = (np.hsplit(self.matrix, mdimm))
        return tupla