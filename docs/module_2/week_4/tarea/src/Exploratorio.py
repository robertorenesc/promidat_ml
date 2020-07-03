import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqplot
from sklearn.preprocessing import StandardScaler
import pandas as pd

class Exploratorio:

    # Constructor
    def __init__(self, datos = None, usar_escala = False, usar_dummy = False):
        preilimary_data = datos
        columns = datos.columns
        if usar_dummy:
            preilimary_data = pd.get_dummies(preilimary_data)
            columns = preilimary_data.columns
        if usar_escala:
            preilimary_data = StandardScaler().fit_transform(preilimary_data)
        self.__datos = pd.DataFrame(preilimary_data, index = datos.index.tolist(), columns = columns)

    def analisis(self, columnas = [], columna_normalidad = "energy"):
        self.mostrar_encabezado()
        self.mostrar_dimension()
        self.mostrar_estadisticas()
        self.mostrar_percentiles()
        self.mostrar_valores_atipicos(columnas)
        self.dibujar_boxplot(columnas)
        self.mostrar_distribucion_densidad()
        self.mostrar_histogramas()
        self.mostrar_test_normalidad(alpha = 0.5, column = columna_normalidad)

    def mostrar_encabezado(self):
        print("\nENCABEZADO")
        print("----------")
        print(self.datos.head())

    def mostrar_dimension(self):
        pass

    def mostrar_estadisticas(self):
        print("\nESTADISTICAS")
        print("------------")
        print(self.datos.dropna().describe())
        print(self.datos.describe())
        print(self.datos.mean(numeric_only=True))
        print(self.datos.median(numeric_only=True))
        print(self.datos.std(numeric_only=True))
        print(self.datos.max(numeric_only=True))

    def mostrar_percentiles(self):
        print("\nPERCENTILES")
        print("-----------")
        print(self.datos.quantile(np.array([0,.25,.50,.75,1])))

    def mostrar_valores_atipicos(self, columns = []):
        print("\nVALORES ATIPICOS POR COLUMNA")
        print("------------------------------")
        variable_names = self.__obtener_columnas(columns)
        for column in variable_names:
            plt.figure(variable_names.index(column))
            self.datos.boxplot(column = column,return_type = 'dict', rot = 45)

    def dibujar_boxplot(self, columns = []):
        plt.figure(20)
        print("\nGRÁFICO DE DISPERSIÓN")
        print("-----------------------")
        variable_names = self.__obtener_columnas(columns)
        sns.pairplot(self.datos, vars = variable_names, height=5)

    def mostrar_distribucion_densidad(self):
        print("\nGRÁFICO DE DENSIDAD")
        print("---------------------")
        caracteristicas = self.datos.T
        plt.scatter(caracteristicas[0], caracteristicas[1], alpha=0.2,s=100*caracteristicas[3], c = self.datos.target, cmap='viridis')
        plt.xlabel(self.datos.feature_names[0])
        plt.ylabel(self.datos.feature_names[1])

    def mostrar_histogramas(self):
        plt.style.use('seaborn-white')
        plt.hist(self.datos)

    def mostrar_test_normalidad(self, alpha = 0.5, column = ""):
        values = self.datos[column].values
        self.test_saphiro_wilk(alpha = alpha, values = values)
        self.test_kolmogorov_smirnov(alpha = alpha, values = values)
        qqplot(values, line='s')
    
    def test_saphiro_wilk(self, alpha = 0.5, values = []):
        print("\nTEST NORMALIDAD SAPHIRO WILK")
        print("------------------------------")
        # print(self.datos.shape)
        shapiro_result = stats.shapiro(values)
        print(f"Results = {shapiro_result}")
        p_value1 = shapiro_result[1]
        if p_value1 > alpha:
            print("La grafica sigue la curva, la muestra proviene de una distribución normal")
        else:
            print("La grafica NO sigue la curva, la muestra NO proviene de una distribución normal")

    def test_kolmogorov_smirnov(self, alpha = 0.5, values = []):
        print("\nTEST NORMALIDAD KOLGOMOROV SMIRNOV")
        print("------------------------------------")
        #print(self.datos.shape)
        ks_results = stats.kstest(values, cdf='norm')
        print(f"Results = {ks_results}")
        p_value2 = ks_results[1]
        if p_value2 > alpha:
            print("La grafica sigue la curva, la muestra proviene de una distribución normal")
        else:
            print("La grafica NO sigue la curva, la muestra NO proviene de una distribución normal")

    def __obtener_columnas(self, columns):
        variable_names = columns
        if len(columns) == 0:
            variable_names = list(self.datos.columns.values)
        return variable_names

    @property 
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self, datos):
        self.__datos = datos
