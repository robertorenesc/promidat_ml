from abc import ABC, abstractmethod
from pandas import DataFrame, pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from ..calcs.IndexesCalculator import IndexesCalculator


# Inheriting from ABC makes this class abstract, cannot be instanciated
class GenericModel(ABC):

    def __init__(self, data = DataFrame):
        # Public access properties
        self.__data = data
        self.__X = None  # Variables used to predict the result
        self.__Y = None  # Variables to be predicted
        self.__classifier_instance = None
        self.__confusion_matrix = None
        self.__prediction = None
        self.__X_train = None # Set of training variables
        self.__X_test = None  # Set of testing the result of predictions
        self.__y_train = None # Set of training results
        self.__y_test = None  # Set of testing results
        self.__indexes = None

    # Abstract methods can have implementation in Python and subclass 
    # can use super() to invoke them
    def build_model(self, variable_predict, train_size = 0.7):
        self.X = self.data.loc[:,self.data.columns != variable_predict]
        self.Y = self.data.loc[:,self.data.columns == variable_predict]
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(self.X, self.Y, train_size = train_size, random_state = 0)

    def plot_importance(self):
        importance = self.classifier_instance.feature_importances_
        labels = self.__X_train.columns.values
        y_pos = np.arange(len(labels))
        plt.barh(y_pos, importance, align='center', alpha=0.5)
        plt.yticks(y_pos, labels)

    def read_parameter(self, metadata: dict, parameter: str, default: None):
        return metadata[parameter] if parameter in metadata else default

    # @abstractmethod
    # def build_model_with_data(self, variable_predict, train_df: DataFrame, test_df: DataFrame):
    #     pass

    def print_testing_info(self):
        print("\nVariables Predictoras:\n")
        print(self.X.head())
        print("\nVariable a Predecir:\n")
        print(self.Y.head())
        #print("\nLas predicciones en Testing son:\n")
        #print(self.prediction)

    def calculate_indexes(self):
        self.__build_confusion_matrix()
        self.indexes = IndexesCalculator(self.confusion_matrix)

    def print_indexes_info(self):
        if self.indexes is None:
            self.calculate_indexes()
        print(f"\nPrecisión Global: {self.indexes.accurancy}")
        print(f"\nPrecisión por Categoría:\n")
        print(self.indexes.category_precisions)

    @abstractmethod
    def train_model(self, metadata: dict):
        pass

    def __build_confusion_matrix(self):
        if self.__prediction is None:
            raise Exception("The model should be trained before get the confusion matrix")
        self.create_confusion_matrix(self.__y_test, self.__prediction, self.classifier_instance.classes_)

    def create_confusion_matrix(self, test, prediction, columns):
        matrix = confusion_matrix(test, prediction)
        if columns is not None:
            self.confusion_matrix = pd.DataFrame(matrix, index = columns, columns = columns)
        else:
            self.confusion_matrix = pd.DataFrame(matrix)
        self.indexes = IndexesCalculator(self.confusion_matrix)

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
    def X_train(self):
        return self.__X_train
    
    @X_train.setter
    def X_train(self, X_train):
        self.__X_train = X_train

    @property
    def y_train(self):
        return self.__y_train
    
    @y_train.setter
    def y_train(self, y_train):
        self.__y_train = y_train

    @property
    def X_test(self):
        return self.__X_test
    
    @X_test.setter
    def X_test(self, X_test):
        self.__X_test = X_test

    @property
    def y_test(self):
        return self.__y_test
    
    @y_test.setter
    def y_test(self, y_test):
        self.__y_test = y_test

    @property 
    def confusion_matrix(self):
        if self.__confusion_matrix is None:
            self.__build_confusion_matrix()
        return self.__confusion_matrix
    
    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        self.__confusion_matrix = confusion_matrix

    @property 
    def classifier_instance(self):
        return self.__classifier_instance
    
    @classifier_instance.setter
    def classifier_instance(self, classifier_instance):
        self.__classifier_instance = classifier_instance

    @property 
    def prediction(self):
        return self.__prediction
    
    @prediction.setter
    def prediction(self, prediction):
        self.__prediction = prediction
    
    @property
    def indexes(self):
        return self.__indexes
    
    @indexes.setter
    def indexes(self, indexes):
        self.__indexes = indexes