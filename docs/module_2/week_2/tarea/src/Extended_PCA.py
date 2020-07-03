import numpy as numpy
import pandas as pandas
from sklearn.preprocessing import StandardScaler
import scipy.linalg as linalg
import os

class Extended_PCA:

    # Constructor
    def __init__(self, data = []):
        self.__data = data
        self.setup_variables()

    # Public methods
    def setup_variables(self):
        self.__center_and_reduce()
        self.__calculate_correlation_matrix()
        self.__calculate_eigen_values()
        self.__calculate_principal_components_matrix()
        self.__calculate_explained_variance()
        self.__calculate_squared_cosines()
        self.__calculate_components_coordinates()

    def print_required_values(self):
        print("Extended_PCA => eigenvalues_: ")
        print(self.eigen_values)
        print("Extended_PCA =>  column_correlations: ")
        print(self.principal_componets_matrix)
        print("Extended_PCA =>  row_cosine_similarities: ")
        print(self.squared_cosines)
        print("Extended_PCA =>  row_coordinates: ")
        print(self.components_coordinates)
        print("Extended_PCA =>  correlation_matrix: ")
        print(self.correlation_matrix)

    # Private methods
    def __center_and_reduce(self):
        # Colocar todos los valores en una escala común
        self.standard_matrix = pandas.DataFrame(StandardScaler().fit_transform(self.data))

    def __calculate_correlation_matrix(self):
        # 2. Calcular la matriz de correlaciones R
        self.correlation_matrix = self.standard_matrix.corr()
        self.correlation_matrix = self.correlation_matrix.set_index(self.data.columns.values)

    def __calculate_eigen_values(self):
        # 3. Calcular valores y vectores propios de R
        self.eigen_values, self.partial_eigen_vectors = linalg.eig(self.correlation_matrix)
        self.eigen_values = [numpy.abs(i) * 10 for i in self.eigen_values]
        self.eigen_vectors = []
        size = len(self.partial_eigen_vectors)
        for i in range(size):
            vector = ([val[i] for val in self.partial_eigen_vectors])
            self.eigen_vectors.append(vector)

        # 4. Ordenar de mayor a menor los valores propios
        # 5. Construir matriz V ordenada de acuerdo a valor propio con su correspondiente
        #   vector propio ordenado
        n = len(self.eigen_values)
        for i in range(n-1): 
            for j in range(0, (n-i)-1): 
                if self.eigen_values[j] < self.eigen_values[j+1]:
                    
                    temp_val = self.eigen_values[j]
                    self.eigen_values[j] = self.eigen_values[j+1]
                    self.eigen_values[j+1] = temp_val
                    
                    temp_vec = list(self.partial_eigen_vectors[j])
                    self.eigen_vectors[j] = list(self.eigen_vectors[j+1])
                    self.eigen_vectors[j+1] = temp_vec

    def __calculate_principal_components_matrix(self): 
        # 6. Calcular la matriz de componentes principales C
        self.principal_componets_matrix = pandas.DataFrame(numpy.mat(self.standard_matrix) * numpy.mat(self.partial_eigen_vectors))

    def __calculate_explained_variance(self):
        # 6.1. Calcular la varianza explicada
        sum_eigen_values = sum(self.eigen_values)
        #print(sum_eigen_values)
        self.explained_variance = [(i / sum_eigen_values) * 100 for i in self.eigen_values]

    def __calculate_squared_cosines(self):
        # 7. Calcular los Cosenos cuadrados
        squared_coordinates = numpy.square(self.principal_componets_matrix)
        total_squares = squared_coordinates.sum(axis = "columns")
        self.squared_cosines = pandas.DataFrame(squared_coordinates).div(total_squares, axis = "rows")

    def __calculate_components_coordinates(self):
        # 8. Get the correlation matrix to print in the graphic, correlate each principal
        #    component with each column in centered and reduced matrix
        correlation_matrix = []
        for i in self.standard_matrix.columns.values:
            correlation_matrix.append(list(map(lambda c : self.principal_componets_matrix[c].corr(self.standard_matrix[i]), self.principal_componets_matrix.columns)))
        self.components_coordinates = pandas.DataFrame(correlation_matrix, index = self.data.columns.values)

    # Getters and Setters
    @property 
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property 
    def standard_matrix(self):
        return self.__standard_matrix
    
    @standard_matrix.setter
    def standard_matrix(self, standard_matrix):
        self.__standard_matrix = standard_matrix

    @property 
    def correlation_matrix(self):
        return self.__correlation_matrix
    
    @correlation_matrix.setter
    def correlation_matrix(self, correlation_matrix):
        self.__correlation_matrix = correlation_matrix

    @property 
    def components_coordinates(self):
        return self.__components_coordinates
    
    @components_coordinates.setter
    def components_coordinates(self, components_coordinates):
        self.__components_coordinates = components_coordinates

    @property 
    def eigen_values(self):
        return self.__eigen_values
    
    @eigen_values.setter
    def eigen_values(self, eigen_values):
        self.__eigen_values = eigen_values

    @property 
    def eigen_vectors(self):
        return self.__eigen_vectors
    
    @eigen_vectors.setter
    def eigen_vectors(self, eigen_vectors):
        self.__eigen_vectors = eigen_vectors

    @property 
    def squared_cosines(self):
        return self.__squared_cosines
    
    @squared_cosines.setter
    def squared_cosines(self, squared_cosines):
        self.__squared_cosines = squared_cosines

    @property 
    def explained_variance(self):
        return self.__explained_variance
    
    @explained_variance.setter
    def explained_variance(self, explained_variance):
        self.__explained_variance = explained_variance

    @property 
    def principal_componets_matrix(self):
        return self.__principal_componets_matrix
    
    @principal_componets_matrix.setter
    def principal_componets_matrix(self, principal_componets_matrix):
        self.__principal_componets_matrix = principal_componets_matrix

    @property 
    def partial_eigen_vectors(self):
        return self.__partial_eigen_vectors
    
    @partial_eigen_vectors.setter
    def partial_eigen_vectors(self, partial_eigen_vectors):
        self.__partial_eigen_vectors = partial_eigen_vectors