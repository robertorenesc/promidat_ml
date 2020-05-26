from Exploratorio import Exploratorio
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from math import pi

from LinkageMethod import LinkageMethod

class Clusters(Exploratorio):

    # Constructor
    def __init__(self, datos, num_clusters = 3, usar_escala = False, usar_dummuy = False):
        super().__init__(datos, usar_escala, usar_dummuy)
        self.__num_clusters = num_clusters
        self.__hierarchical_method = None
        self.__centers = None
        self.__groups = None

    def imprimir_clusters(self):
        print(self.groups)
        print(self.centers)

    def graficar_barras(self, method = LinkageMethod.SINGLE, metric = "euclidean"):
        plt.figure(1, figsize = (12, 8))
        self.__bar_plot(self.centers, self.datos.columns)

    def graficar_radar(self, method = LinkageMethod.SINGLE, metric = "euclidean"):
        plt.figure(1, figsize = (10, 10))
        self.__radar_plot(self.centers, self.datos.columns)

    def __bar_plot(self, centros, labels, cluster = None, var = None):
        from math import ceil, floor
        from seaborn import color_palette
        colores = color_palette()
        minimo = floor(centros.min()) if floor(centros.min()) < 0 else 0
        def inside_plot(valores, labels, titulo):
            plt.barh(range(len(valores)), valores, 1/1.5, color = colores)
            plt.xlim(minimo, ceil(centros.max()))
            plt.title(titulo)
        if var is not None:
            centros = np.array([n[[x in var for x in labels]] for n in centros])
            colores = [colores[x % len(colores)] for x, i in enumerate(labels) if i in var]
            labels = labels[[x in var for x in labels]]
        if cluster is None:
            for i in range(centros.shape[0]):
                plt.subplot(1, centros.shape[0], i + 1)
                inside_plot(centros[i].tolist(), labels, ('Cluster ' + str(i)))
                plt.yticks(range(len(labels)), labels) if i == 0 else plt.yticks([]) 
        else:
            pos = 1
            for i in cluster:
                plt.subplot(1, len(cluster), pos)
                inside_plot(centros[i].tolist(), labels, ('Cluster ' + str(i)))
                plt.yticks(range(len(labels)), labels) if pos == 1 else plt.yticks([]) 
                pos += 1

    def __radar_plot(self, centros, labels):
        centros = np.array([((n - min(n)) / (max(n) - min(n)) * 100) if 
                            max(n) != min(n) else (n/n * 50) for n in centros.T])
        angulos = [n / float(len(labels)) * 2 * pi for n in range(len(labels))]
        angulos += angulos[:1]
        ax = plt.subplot(111, polar = True)
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)
        
        plt.xticks(angulos[:-1], labels)
        ax.set_rlabel_position(0)
        plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"], 
            color = "grey", size = 8)
        plt.ylim(-10, 100)
        for i in range(centros.shape[1]):
            valores = centros[:, i].tolist()
            valores += valores[:1]
            ax.plot(angulos, valores, linewidth = 1, linestyle = 'solid', 
                    label = 'Cluster ' + str(i))
            ax.fill(angulos, valores, alpha = 0.3)
        plt.legend(loc='upper right', bbox_to_anchor = (0.1, 0.1))

    @property 
    def num_clusters(self):
        return self.__num_clusters
    
    @num_clusters.setter
    def num_clusters(self, num_clusters):
        self.__num_clusters = num_clusters

    @property 
    def hierarchical_method(self):
        return self.__hierarchical_method
    
    @hierarchical_method.setter
    def hierarchical_method(self, hierarchical_method):
        self.__hierarchical_method = hierarchical_method

    @property 
    def centers(self):
        return self.__centers
    
    @centers.setter
    def centers(self, centers):
        self.__centers = centers

    @property 
    def groups(self):
        return self.__groups
    
    @groups.setter
    def groups(self, groups):
        self.__groups = groups
