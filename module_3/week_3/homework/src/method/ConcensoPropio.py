from pandas import DataFrame
import pandas as pd
import numpy as np
import functools 
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from method.ModelIndexCalculator import IndexesCalculator
from utils.DataFrameUtils import DataFrameUtils

class ConcensoPropio:

    def __init__(self, probability = True):
        self.__kn_classifier = None
        self.__dec_tree_classifier = None
        self.__ada_classifier = None
        self.__xg_classifier = None
        self.__models = None
        self.__prediction = []
        self.__init_models()
    
    def __init_models(self):
        self.kn_classifier = KNeighborsClassifier()
        self.dec_tree_classifier = DecisionTreeClassifier()
        self.ada_classifier = AdaBoostClassifier()
        self.xg_classifier = GradientBoostingClassifier()
        self.__models = [
            {"model": self.kn_classifier}, 
            {"model": self.dec_tree_classifier}, 
            {"model": self.ada_classifier}, 
            {"model": self.xg_classifier}
        ]

    def fit(self, X_train, y_train):
        for model in self.__models:
            X_sample, y_sample = self.__generate_bootstraps(X_train, y_train, 10)
            model["X_train"] = X_sample
            model["y_train"] = y_sample
            model["model"].fit(X_sample, y_sample.iloc[:,0].values)

    def predict(self, X_test, y_test):
        for model in self.__models:
            model["prediction_proba"] = model["model"].predict_proba(X_test)
            model["prediction"] = model["model"].predict(X_test)
            model["precision_global"] = self.__get_precision_global(model, y_test)
        self.__build_prediction_concenso()
        self.__build_confusion_matrix(y_test)

    def __build_prediction_concenso(self):
        results = DataFrame(self.__models)
        print(results)
        results["weight"] = results["precision_global"] / results["precision_global"].sum()

        for i in range(len(self.__models[0]["prediction_proba"])):
            self.prediction.append(self.__get_prediction(i, results["weight"].values)["category"])
        
    def __get_prediction(self, index, weights):
        predict_0 = self.__get_element_prediction(self.__models[0]["prediction_proba"][index], weights[0])
        predict_1 = self.__get_element_prediction(self.__models[1]["prediction_proba"][index], weights[1])
        predict_2 = self.__get_element_prediction(self.__models[2]["prediction_proba"][index], weights[2])
        predict_3 = self.__get_element_prediction(self.__models[3]["prediction_proba"][index], weights[3])
        return functools.reduce(lambda a,b: a if a["value"] > b["value"] else b, [predict_0, predict_1, predict_2, predict_3])

    def __get_element_prediction(self, prediction, weight):
        prediction = {"value": prediction[0], "category": "Femenino"} if prediction[0] > prediction[1] else {"value": prediction[1], "category": "Masculino"}
        prediction["value"] = prediction["value"] * weight
        return prediction
   
    def __get_precision_global(self, model, y_test):
        matrix = pd.DataFrame(confusion_matrix(y_test, model["prediction"]), index = model["model"].classes_, columns = model["model"].classes_)
        calculator = IndexesCalculator(matrix)
        return calculator.accurancy

    def __generate_bootstraps(self, X_train: DataFrame, y_train: DataFrame, size = 500):
        np.random.seed()
        indexes = np.random.randint(0, len(X_train) , size=size)
        X_sample = X_train.iloc[indexes]
        y_sample = y_train.iloc[indexes]
        return X_sample, y_sample

    def __build_confusion_matrix(self, y_test):
        matrix = confusion_matrix(y_test, self.prediction)
        instance_classifier = self.__models[0]["model"]
        self.confusion_matrix = pd.DataFrame(matrix, index = instance_classifier.classes_, columns = instance_classifier.classes_)

    def print_indexes_info(self):
        self.indexes = IndexesCalculator(self.confusion_matrix)
        print(f"\nPrecisión Global: {self.indexes.accurancy}")
        print(f"\nPrecisión por Categoría:\n")
        print(self.indexes.category_precisions)

    @property
    def kn_classifier(self):
        return self.__kn_classifier
    
    @kn_classifier.setter
    def kn_classifier(self, kn_classifier):
        self.__kn_classifier = kn_classifier

    @property
    def dec_tree_classifier(self):
        return self.__dec_tree_classifier
    
    @dec_tree_classifier.setter
    def dec_tree_classifier(self, dec_tree_classifier):
        self.__dec_tree_classifier = dec_tree_classifier
    
    @property
    def ada_classifier(self):
        return self.__ada_classifier
    
    @ada_classifier.setter
    def ada_classifier(self, ada_classifier):
        self.__ada_classifier = ada_classifier

    @property
    def xg_classifier(self):
        return self.__xg_classifier
    
    @xg_classifier.setter
    def xg_classifier(self, xg_classifier):
        self.__xg_classifier = xg_classifier

    @property
    def prediction(self):
        return self.__prediction
    
    @prediction.setter
    def prediction(self, prediction):
        self.__prediction = prediction

    @property
    def confusion_matrix(self):
        return self.__confusion_matrix
    
    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        self.__confusion_matrix = confusion_matrix