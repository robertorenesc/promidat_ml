import pandas as pandas
import os

from Agregacion import Agregacion

data = pandas.read_csv("EjemploEstudiantes.csv", delimiter = ";", decimal = ".", index_col = 0)
agregacion = Agregacion()
matriz_distancias = agregacion.calcular_distancias(data)
print(matriz_distancias)
print(agregacion.construir_dendrograma(matriz_distancias))

    
