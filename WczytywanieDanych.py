import numpy as np

filename = "test.txt"
print("Odczytywanie wektorów z pliku" + filename)
file = open(filename, "r")

x, y, z = np.loadtxt(file, delimiter=',',unpack=True)

print("Wektor X: ")
print(x)
print("Wektor Y: ")
print(y)
print("Wektor Z: ")
print(z)