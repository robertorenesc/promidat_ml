import ipyvolume as ipv
import pandas as pd
import numpy as np

from sklearn.svm import SVC

class CustomSVM:

    def __init__(self, data:pd.DataFrame):
        self.__data = data
        self.__X = None
        self.__Y = None
        self.__clf = None

    def build_model(self):
        variable_predict = "color"
        self.X = self.data.loc[:,self.data.columns != variable_predict]
        self.Y = self.data.loc[:,self.data.columns == variable_predict]
        self.__clf = SVC(kernel = "linear")
        self.__clf.fit(self.X,self.Y.iloc[:,0].values)

    def draw_plots(self):
        ipv.figure(width=800, height=600)
        self.data.apply(lambda row: self.__draw_plot(row.x, row.y, row.z, row.color), axis = 1)
        ipv.show()

    def draw_support_vectors(self):
        # tmp = np.linspace(0,5,30)
        # x,y = np.meshgrid(tmp,tmp)
        # z = lambda x, y: 2 - y
        # ipv.plot_surface(x, y, z(x, y), color="gray")
        ipv.scatter(self.clf.support_vectors_[:,0], self.clf.support_vectors_[:,1], self.clf.support_vectors_[:,2],  color="orange", size = 3, marker="diamond")

    def draw_hyperplane(self):
        tmp = np.linspace(0,5,30) # Genera 30 puntos entre -0 y 5
        x,y = np.meshgrid(tmp,tmp) # Genera las coordenadas para dibujar X y Y del plano
        # apply_w_formula es la fórmula para determinar Z en base a los generados en la 
        # anterior instrucción 
        ipv.plot_surface(x, y, self.apply_w_formula(self.__clf,x, y), color="yellow")

    def apply_w_formula(self, clf, x, y):
        return (-clf.intercept_[0]-clf.coef_[0][0]*np.array(x) -clf.coef_[0][1]*np.array(y)) / clf.coef_[0][2]

    def __draw_plot(self, x:int, y:int, z:int, color:str):
        x_arr = np.array([x])
        y_arr = np.array([y])
        z_arr = np.array([z])
        ipv.scatter(x_arr, y_arr, z_arr, color = color,size = 3, marker="sphere")

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def X(self):
        return self.__X
    
    @X.setter
    def X(self, X):
        self.__X = X

    @property
    def Y(self):
        return self.__Y
    
    @Y.setter
    def Y(self, Y):
        self.__Y = Y

    @property
    def clf(self):
        return self.__clf
    
    @clf.setter
    def clf(self, clf):
        self.__clf = clf