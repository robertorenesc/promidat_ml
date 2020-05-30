from IndexesCalculator import IndexesCalculator
from sklearn.metrics import confusion_matrix
import seaborn as sns
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors

class QualityModel:

    # Constructor
    def __init__(self, data):
        self.__calculator = IndexesCalculator(data)
        self.__data = data

    def predictive_power_by_variable(self):
        for column in self.data.columns[:-1]:
            self.numeric_predictive_power(column, "genero")

    def numeric_predictive_power(self, var:str, variable_predict:str):
        sns.FacetGrid(self.data, hue=variable_predict, height=6).map(sns.kdeplot, var, shade=True).add_legend()

    def poder_predictivo_categorica(self, var:str, variable_predict:str):
        df = pd.crosstab(index= self.data[var],columns=self.data[variable_predict])
        df = df.div(df.sum(axis=1),axis=0)
        titulo = "Distribución de la variable %s según la variable %s" % (var,variable_predict)
        g = df.plot(kind='barh',stacked=True,legend = True, figsize = (10,9), \
                    xlim = (0,1),title = titulo, width = 0.8)
        vals = g.get_xticks()
        g.set_xticklabels(['{:.0%}'.format(x) for x in vals])
        g.legend(loc='upper center', bbox_to_anchor=(1.08, 1), shadow=True, ncol=1)
        for bars in g.containers:
            plt.setp(bars, width=.9)
        for i in range(df.shape[0]):
            countv = 0 
            for v in df.iloc[i]:
                g.text(np.mean([countv,countv+v]) - 0.03, i , '{:.1%}'.format(v), color='black', fontweight='bold')
                countv = countv + v

    def distribution_predict_variable(self, variable_predict:str):
        colors = list(dict(**mcolors.CSS4_COLORS))
        df = pd.crosstab(index=self.data[variable_predict],columns="valor") / self.data[variable_predict].count()
        fig = plt.figure(figsize=(10,9))
        g = fig.add_subplot(111)
        countv = 0
        titulo = "Distribución de la variable %s" % variable_predict
        for i in range(df.shape[0]):
            g.barh(1,df.iloc[i],left = countv, align='center',color=colors[11+i],label= df.iloc[i].name)
            countv = countv + df.iloc[i]
        vals = g.get_xticks()
        g.set_xlim(0,1)
        g.set_yticklabels("")
        g.set_title(titulo)
        g.set_ylabel(variable_predict)
        g.set_xticklabels(['{:.0%}'.format(x) for x in vals])
        countv = 0 
        for v in df.iloc[:,0]:
            g.text(np.mean([countv,countv+v]) - 0.03, 1 , '{:.1%}'.format(v), color='black', fontweight='bold')
            countv = countv + v
        g.legend(loc='upper center', bbox_to_anchor=(1.08, 1), shadow=True, ncol=1)

    @property 
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data