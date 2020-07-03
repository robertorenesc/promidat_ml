from utils.ACP import ACP
import pandas as pandas
import matplotlib.pyplot as plt

class ACPPersonalizado(ACP):

    # Constructor
    def __init__(self, datos, n_componentes = 5, columnas = []):
        datos_filtrados = pandas.DataFrame(datos, columns = columnas)
        super().__init__(datos = datos_filtrados, n_componentes = n_componentes)

    def plot_plano_principal(self, ejes = [0, 1], ind_labels = True, titulo = 'Plano Principal', cos2_min = 0):
        bien_representados = self.__obtener_bien_representados(ejes, cos2_min)
        coordenadas_bien_representados = self.coordenadas_ind[self.coordenadas_ind.index.isin(values = bien_representados)]
        x = coordenadas_bien_representados[ejes[0]].values
        y = coordenadas_bien_representados[ejes[1]].values
        plt.subplots(figsize=(13, 13))
        plt.style.use('seaborn-whitegrid')
        plt.scatter(x, y, color = 'gray')
        plt.title(titulo)
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.var_explicada[ejes[0]], 2)
        inercia_y = round(self.var_explicada[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        if ind_labels:
            for i, txt in enumerate(coordenadas_bien_representados.index):
                plt.annotate(txt, (x[i], y[i]))

    def plot_sobreposicion(self, ejes = [0, 1], ind_labels = True, 
                      var_labels = True, titulo = 'Sobreposición Plano-Círculo', cos2_min = 0):
        bien_representados = self.__obtener_bien_representados(ejes, cos2_min)
        coordenadas_bien_representados = self.coordenadas_ind[self.coordenadas_ind.index.isin(values = bien_representados)]
        x = coordenadas_bien_representados[ejes[0]].values
        y = coordenadas_bien_representados[ejes[1]].values
        cor = self.correlacion_var.iloc[:, ejes]
        scale = min((max(x) - min(x)/(max(cor[ejes[0]]) - min(cor[ejes[0]]))), 
                    (max(y) - min(y)/(max(cor[ejes[1]]) - min(cor[ejes[1]])))) * 0.7
        cor = self.correlacion_var.iloc[:, ejes].values
        plt.subplots(figsize=(13, 13))
        plt.style.use('seaborn-whitegrid')
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.var_explicada[ejes[0]], 2)
        inercia_y = round(self.var_explicada[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        plt.scatter(x, y, color = 'gray')
        if ind_labels:
            for i, txt in enumerate(coordenadas_bien_representados.index):
                plt.annotate(txt, (x[i], y[i]))
        for i in range(cor.shape[0]):
            plt.arrow(0, 0, cor[i, 0] * scale, cor[i, 1] * scale, color = 'steelblue', 
                      alpha = 0.5, head_width = 0.05, head_length = 0.05)
            if var_labels:
                plt.text(cor[i, 0] * scale * 1.15, cor[i, 1] * scale * 1.15, 
                         self.correlacion_var.index[i], 
                         color = 'steelblue', ha = 'center', va = 'center')  

    def __obtener_bien_representados(self, ejes, cos2_min):
        return super().cos2_ind.loc[lambda df: (df[ejes[0]] >= cos2_min) & (df[ejes[1]] >= cos2_min)].index.values
        