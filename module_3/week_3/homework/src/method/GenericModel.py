from abc import ABC, abstractmethod
from pandas import DataFrame
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

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
        # Private properties
        self.__X_train = None # Set of training variables
        self.__X_test = None  # Set of testing the result of predictions
        self.__y_train = None # Set of training results
        self.__y_test = None  # Set of testing results

    # Abstract methods can have implementation in Python and subclass 
    # can use super() to invoke them
    def build_model(self, variable_predict, train_size = 0.7):
        self.X = self.data.loc[:,self.data.columns != variable_predict]
        self.Y = self.data.loc[:,self.data.columns == variable_predict]
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(self.X, self.Y, train_size = train_size, random_state = 0)

    # @abstractmethod
    # def build_model_with_data(self, variable_predict, train_df: DataFrame, test_df: DataFrame):
    #     pass

    @abstractmethod
    def train_model(self, methadata: dict):
        pass

    @abstractmethod
    def plot_prediction(self):
        pass

    def __build_confusion_matrix(self):
        if self.__prediction is None:
            raise Exception("The model should be trained before get the confusion matrix")
        matrix = confusion_matrix(self.__y_test, self.__prediction)
        self.confusion_matrix = pd.DataFrame(matrix, index = self.classifier_instance.classes_, columns = self.classifier_instance.classes_)

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
    def confusion_matrix(self):
        if self.confusion_matrix is None:
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