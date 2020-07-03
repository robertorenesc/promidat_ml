# from Process import Process
# from LinkageMethod import LinkageMethod

# import pandas as pd
# import os
# import numpy as np
# from sklearn.preprocessing import StandardScaler
# from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
# import matplotlib.pyplot as plt
# from scipy.spatial.distance import pdist
# from math import pi


# data = [[0, 5, 2, 3],
#         [5, 0, 1, 7],
#         [2, 1, 0, 6],
#         [3, 7, 6, 0]]

# print(linkage(data, method='single', metric='euclidean'))

from ExtendedProcess import ExtendedProcess

process4 = ExtendedProcess()
process4.load_data(path = "./resources", file = "EjemploEstudiantes.csv", delimiter = ";", decimal = ",")
process4.calculate_distances_matrix()
