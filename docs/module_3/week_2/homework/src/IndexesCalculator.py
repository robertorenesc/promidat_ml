import numpy as np
import pandas as pd

class IndexesCalculator:

    def __init__(self, confusion_matrix):
        self.__confusion_matrix = confusion_matrix
        self.__matrix = confusion_matrix.to_numpy()
        self.__accurancy = None
        self.__error_rate = None
        self.__category_precisions = pd.DataFrame()
        self.__false_by_category = None
        self.__assertiveness_by_category = None

    def show_confusion_matrix_indexes(self): 
        print(f"Matriz de Confusión: \n{self.confusion_matrix}\n")
        print(f"Precisión Global: {self.accurancy}")
        print(f"Error Global: {self.error_rate}")
        print(f"Precision por Categoría:\n{self.category_precisions}\n")
        print(f"Falsos Positivos por Categoría: \n{self.false_by_category}\n")
        print(f"Asertividad por Categoría: \n{self.assertiveness_by_category}\n")

    def get_indexes_dictionary(self):
        indexes = {
            "Precisión Global": self.accurancy,
            "Error Global": self.error_rate
        }
        for col in self.category_precisions.columns:
            indexes[f"Precisión {col}"] = self.__category_precisions[col].iloc[0]
        for col in self.false_by_category.columns:
            indexes[f"Falso Positivo {col}"] = self.__false_by_category[col].iloc[0]
        for col in self.assertiveness_by_category.columns:
            indexes[f"Asertividad {col}"] = self.__false_by_category[col].iloc[0]
        return indexes

    @property 
    def confusion_matrix(self):
        return self.__confusion_matrix
    
    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        self.__confusion_matrix = confusion_matrix

    @property 
    def accurancy(self):
        if self.__accurancy == None:
            self.__accurancy = np.sum(self.__matrix.diagonal()) / np.sum(self.__matrix)
        return self.__accurancy
    
    @accurancy.setter
    def accurancy(self, accurancy):
        self.__accurancy = accurancy

    @property 
    def error_rate(self):
        if self.__error_rate == None:
            self.__error_rate = 1 - self.accurancy
        return self.__error_rate
    
    @error_rate.setter
    def error_rate(self, error_rate):
        self.__error_rate = error_rate

    @property 
    def category_precisions(self):
        if self.__category_precisions.empty:
            self.__category_precisions = pd.DataFrame(self.__matrix.diagonal() / np.sum(self.__matrix, axis = 1)).T
            self.__category_precisions.columns = self.confusion_matrix.columns
        return self.__category_precisions
    
    @category_precisions.setter
    def category_precisions(self, category_precisions):
        self.__category_precisions = category_precisions

    @property 
    def false_by_category(self):
        if self.__false_by_category == None:
            self.__false_by_category = pd.DataFrame(np.fliplr(self.__matrix).diagonal() / np.sum(self.__matrix, axis = 1)).T
            self.__false_by_category.columns = self.confusion_matrix.columns
        return self.__false_by_category
    
    @false_by_category.setter
    def false_by_category(self, false_by_category):
        self.__false_by_category = false_by_category

    @property 
    def assertiveness_by_category(self):
        if self.__assertiveness_by_category == None:
            self.__assertiveness_by_category = pd.DataFrame(self.__matrix.diagonal() / np.sum(self.__matrix, axis = 0)).T
            self.__assertiveness_by_category.columns = self.confusion_matrix.columns
        return self.__assertiveness_by_category
    
    @assertiveness_by_category.setter
    def assertiveness_by_category(self, assertiveness_by_category):
        self.__assertiveness_by_category = assertiveness_by_category