import math
import pandas as pd
from TipoSalto import TipoSalto

class Agregacion:

    # Constructor
    def __init__(self,  tipo_salto = TipoSalto.SALTO_MINIMO):
        self.__tipo_salto = tipo_salto

    def calcular_distancias(self, data):
        matriz = data.values
        distances = []
        for i in range(len(data)):
            distance = []
            for j in range(len(data)):
                if j < i:
                    distance.append(None)
                else:
                    distance.append(self.__calcular_distancia_vector(matriz[i], matriz[j]))
            distances.append(distance)
        return pd.DataFrame(distances)
    
    def construir_dendrograma(self, data):
        return self.__obtener_menor_valor(data)

    def __obtener_menor_valor(self, data):
        menor_valor = None
        coordenadas = (0,0)
        matriz = data.to_numpy()
        for i in range(len(matriz)):
            for j in range(i, len(matriz)):
                if j > i:
                    if menor_valor == None or menor_valor > matriz[i][j]:
                        menor_valor = matriz[i][j]
                        coordenadas = (i, j)
        return menor_valor, coordenadas

    def __obtener_menor_valor_row(self, vector):
        menor_valor = 0
        for i in range(len(vector)):
            if (vector[i] == 0 or vector[i] == None) or menor_valor > vector[i]:
                menor_valor = vector[i]
        return menor_valor

    def __calcular_distancia_vector(self, vector1, vector2):
        distancia = 0.0
        for i in range(len(vector1)):
            distancia += math.pow((vector1[i] - vector2[i]), 2)
        return math.sqrt(distancia)


