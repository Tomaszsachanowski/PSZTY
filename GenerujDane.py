"""
autorzy:
    Aleksander Krzemiński,
    Tomasz Sachanowski 
"""

import numpy as np
from sklearn.decomposition import PCA

def iris_two_collection(iris, num_one, num_two):
        X_reduced = PCA(n_components=3).fit_transform(iris.data)
        # przekształcam dane na połoznie w przestrzeni
        if num_one == 0:
                if num_two == 1:
                        a = np.append(X_reduced[0:50,], np.ones((len(X_reduced[0:50,]), 1)), axis=1)
                        b = np.append(X_reduced[50:100,], np.ones((len(X_reduced[50:100,]), 1)), axis=1)
                        c = np.append(X_reduced[100:,], np.zeros((len(X_reduced[100:,]), 1)), axis=1)
                if num_two == 2:
                        a = np.append(X_reduced[0:50,], np.ones((len(X_reduced[0:50,]), 1)), axis=1)
                        b = np.append(X_reduced[50:100,], np.zeros((len(X_reduced[50:100,]), 1)), axis=1)
                        c = np.append(X_reduced[100:,], np.ones((len(X_reduced[100:,]), 1)), axis=1)
        else:
                a = np.append(X_reduced[0:50,], np.ones((len(X_reduced[0:50,]), 1)), axis=1)
                b = np.append(X_reduced[50:100,], np.zeros((len(X_reduced[50:100,]), 1)), axis=1)
                c = np.append(X_reduced[100:,], np.zeros((len(X_reduced[100:,]), 1)), axis=1)

        x = np.vstack([a, b])
        x = np.vstack([x, c])
        return x 
