import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from math import pi

from LinkageMethod import LinkageMethod
from ACP import ACP

class Process:

    # Constructor
    def __init__(self):
        self.__data = None
        self.__hierarchical_method = None
        self.__centers = None
        self.__groups = None

    def load_data(self, path = "", file = "", delimiter = ";", decimal = ".", index_col = 0, columns_to_exclude = [], recode_colums = [], use_dummies = False):
        os.chdir(path)
        preilimary_data = pd.read_csv(file, delimiter = delimiter, decimal = decimal, index_col = index_col)
        
        if len(columns_to_exclude) > 0:
            preilimary_data = preilimary_data.drop(columns_to_exclude, 1)

        if use_dummies:
            preilimary_data = pd.get_dummies(preilimary_data)

        # Centrar y reducir
        self.data = pd.DataFrame(StandardScaler().fit_transform(preilimary_data), index = preilimary_data.index.tolist())
        self.data.columns = preilimary_data.columns
        
        print(self.data)

    def idenfity_hierarchical_cluster(self, method = LinkageMethod.SINGLE):
        self.hierarchical_method = self.__get_linkage_method(method)
        
    def plot_dendogram(self, cut_values = []):
        plt.figure(figsize=(20,20))
        dendrogram(self.hierarchical_method,labels = self.data.index.tolist())
        for cut in cut_values:
            self.__add_cut_to_dendogram(cut["value"], cut["text"])

    def __add_cut_to_dendogram(self, cut_value = None, cut_text = ""):
        ax = plt.gca()
        limites = ax.get_xbound()
        ax.plot(limites, [cut_value, cut_value], '--', c = 'k')
        ax.text(limites[1], cut_value, cut_text, va = 'center', fontdict = {'size': 15})

    def draw_bars(self, method = LinkageMethod.SINGLE, metric = "euclidean", num_clusters = 3):
        self.__setup_groups_and_centers(method = method, num_clusters = num_clusters)
        plt.figure(1, figsize = (12, 8))
        self.__bar_plot(self.centers, self.data.columns)

    def draw_radar(self, method = LinkageMethod.SINGLE, metric = "euclidean", num_clusters = 3):
        self.__setup_groups_and_centers(method = method, num_clusters = num_clusters)
        plt.figure(1, figsize = (10, 10))
        self.__radar_plot(self.centers, self.data.columns)

    def draw_acp_plain(self):
        acp = ACP(self.data, n_componentes = 3)
        acp.plot_plano_principal(groups = self.groups)

    def __setup_groups_and_centers(self, method = LinkageMethod.SINGLE, metric = "euclidean", num_clusters = 3):
        if self.groups is None:
            groups = fcluster(linkage(pdist(self.data), method = method.value, metric = metric), num_clusters, criterion = 'maxclust')
            self.groups = groups - 1
        
        if self.centers is None:
            array = []
            for i in range(num_clusters):
                array.append(self.centroid(i, self.data, self.groups))
            self.centers = np.array(pd.concat(array))

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

    def centroid(self, num_cluster, data, clusters):
        ind = clusters == num_cluster
        return(pd.DataFrame(data[ind].mean()).T)

    def __get_linkage_method(self, method = LinkageMethod.SINGLE):
        if method == LinkageMethod.SINGLE:
            return single(self.data)
        elif method == LinkageMethod.COMPLETE:
            return complete(self.data)
        elif method == LinkageMethod.AVERAGE:
            return average(self.data)
        else:
            return ward(self.data)

    @property 
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
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