from Clusters import Clusters
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from math import pi

from LinkageMethod import LinkageMethod

class Jerarquico(Clusters):

    # Constructor
    def __init__(self, datos, usar_escala = False, usar_dummy = False, num_clusters = 3, max_iter = 1000, n_init = 100):
        super().__init__(datos = datos, num_clusters = num_clusters, usar_escala = usar_escala, usar_dummuy = usar_dummy)
        self.__max_iter = max_iter
        self.__n_init = n_init

    def analisis(self):
        self.obtener_clusters()
        self.graficar_barras()
        self.graficar_radar()

    def obtener_clusters(self, method = LinkageMethod.SINGLE, metric = "euclidean", num_clusters = 3):
        if self.groups is None:
            groups = fcluster(linkage(pdist(self.datos), method = method.value, metric = metric), num_clusters, criterion = 'maxclust')
            self.groups = groups - 1
        
        if self.centers is None:
            array = []
            for i in range(num_clusters):
                array.append(self.centroid(i, self.datos, self.groups))
            self.centers = np.array(pd.concat(array))
    
    def centroid(self, num_cluster, data, clusters):
        ind = clusters == num_cluster
        return(pd.DataFrame(data[ind].mean()).T)

    def __get_linkage_method(self, method = LinkageMethod.SINGLE):
        if method == LinkageMethod.SINGLE:
            return single(self.datos)
        elif method == LinkageMethod.COMPLETE:
            return complete(self.datos)
        elif method == LinkageMethod.AVERAGE:
            return average(self.datos)
        else:
            return ward(self.datos)

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
    