datos = pd.read_csv("SA.csv", delimiter = ";", decimal = ".", index_col = 0)
numericos = datos
del numericos["famhist"]
del numericos["chd"]

kmedias2 = KMedias(datos = numericos, num_clusters = 3, max_iter = 1000, n_init = 100, usar_escala = True)
print(kmedias2.datos)

