from Clusters import Clusters

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

class KMedias(Clusters):

    # Constructor
    def __init__(self, datos, usar_escala = False, usar_dummy = False, num_clusters = 3, max_iter = 1000, n_init = 100):
        super().__init__(datos = datos, num_clusters = num_clusters, usar_escala = usar_escala, usar_dummuy = usar_dummy)
        self.__max_iter = max_iter
        self.__n_init = n_init

    def analisis(self):
        self.obtener_clusters()
        self.graficar_barras()
        self.graficar_radar()

    def obtener_clusters(self):
        kme = KMeans(n_clusters = self.num_clusters ,max_iter = self.max_iter, n_init = self.n_init)
        kme.fit(self.datos)
        self.groups = kme.predict(self.datos)
        self.centers = np.array(kme.cluster_centers_)

    def graficar_codo_de_jambu(self, num_ejecuciones = 20):
        Nc = range(1, num_ejecuciones)
        kmediasList = [KMeans(n_clusters=i) for i in Nc]
        plt.subplots(figsize=(13, 13))
        varianza = [kmediasList[i].fit(self.datos).inertia_ for i in range(len(kmediasList))]
        plt.plot(Nc,varianza,'o-')
        plt.xlabel('Número de clústeres')
        plt.ylabel('Varianza explicada por cada cluster (Inercia Intraclases)')
        plt.title('Codo de Jambu')

    @property 
    def max_iter(self):
        return self.__max_iter
    
    @max_iter.setter
    def max_iter(self, max_iter):
        self.__max_iter = max_iter

    @property 
    def n_init(self):
        return self.__n_init
    
    @n_init.setter
    def n_init(self, n_init):
        self.__n_init = n_init