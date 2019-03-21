import numpy as np

### Data class ###
# usage: printing 
# and loading data
#  from text file 
class Data:
    def __init__(self, filename):
        self.filename = filename
    
    # load() function -> loads data from txt file 
    def loadToMatrix(self):
        file = open(self.filename, "r")
        return np.loadtxt(file, delimiter=',')

    # split() function -> creates tupla out of matrix columns
    def split(self, matrix):
        mdimm = matrix.shape
        ncol = mdimm[1]
        #hpslit - horizontal split
        tupla = (np.hsplit(matrix, ncol))
        return tupla
