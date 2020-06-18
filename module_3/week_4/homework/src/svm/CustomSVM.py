import ipyvolume as ipv
import pandas as pd
import numpy as np

from method.SVMModel import SVMModel

class CustomSVM:

    def __init__(self, data:pd.DataFrame):
        self.__data = data

    def draw_plots(self):
        ipv.figure()
        self.data.apply(lambda row: self.__draw_plot(row.x, row.y, row.z, row.color), axis = 1)
        ipv.show()


    def __draw_plot(self, x:int, y:int, z:int, color:str):
        x_arr = np.array([x])
        y_arr = np.array([y])
        z_arr = np.array([z])
        ipv.scatter(x_arr, y_arr, z_arr, color = color,size = 3, marker="sphere")

    def draw_hyperplane(self):
        model = SVMModel(self.data)
        model.build_model(variable_predict = "color", train_size = 0.8)
        model.train_model(metadata = {"kernel": "linear"})
        vectors = pd.DataFrame(model.classifier_instance.support_vectors_)
        print(vectors)
        ipv.plot_surface(np.array(vectors.loc[:,0:1]), np.array(vectors.loc[:,1:2]), np.array(vectors.loc[:,0:1]), color="orange")

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data