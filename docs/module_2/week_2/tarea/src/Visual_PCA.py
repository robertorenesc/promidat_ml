from Extended_PCA import Extended_PCA
import matplotlib.pyplot as plt

class Visual_PCA(Extended_PCA):

    def __init__(self, data):
        super().__init__(data)

    def draw_principal_plain(self, ejes = [0, 1], ind_labels = True, titulo = 'Plano Principal'):
        x = self.components_coordinates[ejes[0]].values
        y = self.components_coordinates[ejes[1]].values
        plt.subplots(figsize=(13, 13))
        plt.style.use('seaborn-whitegrid')
        plt.scatter(x, y, color = 'gray')
        plt.title(titulo)
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.explained_variance[ejes[0]], 2)
        inercia_y = round(self.explained_variance[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        if ind_labels:
            for i, txt in enumerate(self.components_coordinates.index):
                plt.annotate(txt, (x[i], y[i]))

    def draw_circle(self, ejes = [0, 1], var_labels = True, titulo = 'Círculo de Correlación'):
        cor = self.correlation_matrix.iloc[:, ejes].values
        plt.style.use('seaborn-whitegrid')
        c = plt.Circle((0, 0), radius = 1, color = 'steelblue', fill = False)
        plt.subplots(figsize=(13, 13))
        plt.gca().add_patch(c)
        plt.axis('scaled')
        plt.title(titulo)
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.explained_variance[ejes[0]], 2)
        inercia_y = round(self.explained_variance[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        for i in range(cor.shape[0]):
            plt.arrow(0, 0, cor[i, 0] * 0.95, cor[i, 1] * 0.95, color = 'steelblue', 
                      alpha = 0.5, head_width = 0.05, head_length = 0.05)
            if var_labels:
                plt.text(cor[i, 0] * 1.05, cor[i, 1] * 1.05, self.correlation_matrix.index[i], 
                         color = 'steelblue', ha = 'center', va = 'center')

    def draw_superposition(self, ejes = [0, 1], ind_labels = True, var_labels = True, titulo = 'Sobreposición Plano-Círculo'):
        x = self.components_coordinates[ejes[0]].values
        y = self.components_coordinates[ejes[1]].values
        cor = self.correlation_matrix.iloc[:, ejes]
        scale = min((max(x) - min(x)/(max(cor[ejes[0]]) - min(cor[ejes[0]]))), 
                    (max(y) - min(y)/(max(cor[ejes[1]]) - min(cor[ejes[1]])))) * 0.7
        cor = self.correlation_matrix.iloc[:, ejes].values
        plt.subplots(figsize=(13, 13))
        plt.style.use('seaborn-whitegrid')
        plt.axhline(y = 0, color = 'dimgrey', linestyle = '--')
        plt.axvline(x = 0, color = 'dimgrey', linestyle = '--')
        inercia_x = round(self.explained_variance[ejes[0]], 2)
        inercia_y = round(self.explained_variance[ejes[1]], 2)
        plt.xlabel('Componente ' + str(ejes[0]) + ' (' + str(inercia_x) + '%)')
        plt.ylabel('Componente ' + str(ejes[1]) + ' (' + str(inercia_y) + '%)')
        plt.scatter(x, y, color = 'gray')
        if ind_labels:
            for i, txt in enumerate(self.components_coordinates.index):
                plt.annotate(txt, (x[i], y[i]))
        for i in range(cor.shape[0]):
            plt.arrow(0, 0, cor[i, 0] * scale, cor[i, 1] * scale, color = 'steelblue', 
                      alpha = 0.5, head_width = 0.05, head_length = 0.05)
            if var_labels:
                plt.text(cor[i, 0] * scale * 1.15, cor[i, 1] * scale * 1.15, 
                         self.correlation_matrix.index[i], 
                         color = 'steelblue', ha = 'center', va = 'center')