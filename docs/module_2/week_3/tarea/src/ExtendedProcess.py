from Process import Process
import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, ward, single, complete,average,linkage, fcluster
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from math import pi

from LinkageMethod import LinkageMethod

class ExtendedProcess(Process):
    
    def __init__(self):
        super().__init__()

    def calculate_distances_matrix(self):
        print(pdist(self.data, metric = self.get_chebychev_formula()))
        print(pdist(self.data, metric = "chebyshev"))

    def get_chebychev_formula(self):
        return lambda x, y: max(abs(x - y))

    def idenfity_hierarchical_cluster(self, num_clusters = 3):
        self.__setup_groups_and_centers(num_clusters = num_clusters)
        self.hierarchical_method = linkage(pdist(self.data, metric = self.get_chebychev_formula()))

    def __setup_groups_and_centers(self, num_clusters = 3):
        if self.groups is None:
            groups = fcluster(linkage(pdist(self.data, metric = self.get_chebychev_formula()), method = "centroid", metric = self.get_chebychev_formula()), num_clusters, criterion = 'maxclust')
            self.groups = groups - 1
        
        if self.centers is None:
            array = []
            for i in range(num_clusters):
                array.append(super().centroid(i, self.data, self.groups))
            self.centers = np.array(pd.concat(array))
