from utils.DataFrameUtils import DataFrameUtils
from utils.QualityModel import QualityModel
from method.KNeighborsModel import KNeighborsModel
from method.RandomForestModel import RandomForestModel
from method.ADABoostingModel import ADABoostingModel
from method.XGBoostingModel import XGBoostingModel
from method.SVMModel import SVMModel
import numpy as np
from sklearn.metrics import confusion_matrix
from method.ModelIndexCalculator import IndexesCalculator


class Runner:

    @staticmethod
    def ejercicio_4():
        data = DataFrameUtils.read_cvs("/mnt/c/Users/rtsz/Learning/promidat_ml/module_3/week_3/homework/src/data/voces.csv", delimiter = ",", decimal = ".", index_col = None)
        X = data.loc[:,data.columns != "genero"]
        Y = data.loc[:,data.columns == "genero"]
        print("\nVariables Predictoras:\n")
        print(X.head())
        print("\nVariable a Predecir:\n")
        print(Y.head())
        X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size = 0.7, random_state = 0)
        model = ConcensoPropio()
        model.fit(X_train = X_train, y_train = y_train)
        model.predict(X_test, y_test)
        model.print_indexes_info()

    @staticmethod
    def ejercicio_1():

        # 1. Carga de datos
        data_voces = DataFrameUtils.read_cvs("/mnt/c/Users/rtsz/Learning/promidat_ml/module_3/week_4/homework/src/data/voces.csv", delimiter = ",", decimal = ".", index_col = None)
        qualityModel = QualityModel(data_voces)
        qualityModel.distribution_predict_variable("genero")

        # 2. Calculando predicciones con SVM
        svmModel = SVMModel(data_voces)
        svmModel.build_model(variable_predict = "genero", train_size = 0.8)
        svmModel.train_model(metadata = {})

        svmModel.print_testing_info()
        svmModel.print_indexes_info()

        # 3. Generación de los modelos anteriores

        # K-Neighbors
        kNeighborsModel = KNeighborsModel(data_voces)
        kNeighborsModel.build_model(variable_predict = "genero", train_size = 0.8)
        kNeighborsModel.train_model(metadata = {})
        kNeighborsModel.calculate_indexes()

        # Random Forest
        randomForestModel = RandomForestModel(data_voces)
        randomForestModel.build_model(variable_predict = "genero", train_size = 0.8)
        randomForestModel.train_model(metadata = {})
        randomForestModel.calculate_indexes()

        # ADA Boosting
        adaBoostingModel = ADABoostingModel(data_voces)
        adaBoostingModel.build_model(variable_predict = "genero", train_size = 0.8)
        adaBoostingModel.train_model(metadata = {})
        adaBoostingModel.calculate_indexes()

        # ADA Boosting
        xgBoostingModel = XGBoostingModel(data_voces)
        xgBoostingModel.build_model(variable_predict = "genero", train_size = 0.8)
        xgBoostingModel.train_model(metadata = {})
        xgBoostingModel.calculate_indexes()


        # 3. Matriz de Comparación
        print("Matriz de Comparación")
        indexes = DataFrameUtils.create_dataframe_from_dict(
            [
                kNeighborsModel.indexes.get_indexes_dictionary(),
                randomForestModel.indexes.get_indexes_dictionary(),
                adaBoostingModel.indexes.get_indexes_dictionary(),
                xgBoostingModel.indexes.get_indexes_dictionary(),
                svmModel.indexes.get_indexes_dictionary()
            ], columns = ["K-Neighbors","Random Forest", "ADA Boosting", "XG Boosting","SVM Model"])
        print(indexes)

        kernels = ['linear', 'poly', 'rbf', 'sigmoid']
        index_kernels = []

        for kernel in kernels:
            model = SVMModel(data_voces)
            model.build_model(variable_predict = "genero", train_size = 0.8)
            model.train_model(metadata = {"kernel" : kernel})
            model.calculate_indexes()
            index_kernels.append(model.indexes.get_indexes_dictionary())
            
        indexes = DataFrameUtils.create_dataframe_from_dict(index_kernels, columns = kernels)
        print(indexes)  

Runner.ejercicio_1()
