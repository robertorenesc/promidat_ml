from KMedias import KMedias
import pandas as pd
import os

os.chdir("./resources")
datos2 = pd.read_csv("SAheart.csv", delimiter = ";", decimal = ".", index_col = 0)
kmedias3 = KMedias(datos = datos2, num_clusters = 3, max_iter = 2000, n_init = 150, usar_escala = True, usar_dummy = True)
print(kmedias3.datos)