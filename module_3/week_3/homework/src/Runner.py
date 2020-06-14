from utils.DataFrameUtils import DataFrameUtils
from utils.QualityModel import QualityModel
from method.RandomForestModel import RandomForestModel
from method.ADABoostingModel import ADABoostingModel
from method.XGBoostingModel import XGBoostingModel
from sklearn.model_selection import train_test_split

from method.ConcensoPropio import ConcensoPropio


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

    @staticmethod
    def ejercicion_1():

        # 1. Carga de datos
        data_voces = DataFrameUtils.read_cvs("/mnt/c/Users/rtsz/Learning/promidat_ml/module_3/week_3/homework/src/data/voces.csv", delimiter = ",", decimal = ".", index_col = None)
        qualityModel = QualityModel(data_voces)
        qualityModel.distribution_predict_variable("genero")

        # 2. Random Forest
        randomForestModel = RandomForestModel(data_voces)
        randomForestModel.build_model(variable_predict = "genero", train_size = 0.8)
        randomForestModel.train_model(metadata = {})

        # 2. ADA Boosting
        adaBoostingModel = ADABoostingModel(data_voces)
        adaBoostingModel.build_model(variable_predict = "genero", train_size = 0.8)
        adaBoostingModel.train_model(metadata = {})

        # 2. ADA Boosting
        xgBoostingModel = XGBoostingModel(data_voces)
        xgBoostingModel.build_model(variable_predict = "genero", train_size = 0.8)
        xgBoostingModel.train_model(metadata = {})

        randomForestModel.print_testing_info()
        randomForestModel.print_indexes_info()
        adaBoostingModel.print_indexes_info()
        xgBoostingModel.print_indexes_info()

        # 2. Matriz de Comparación
        print("Matriz de Comparación")
        indexes = DataFrameUtils.create_dataframe_from_dict(
            [
                randomForestModel.indexes.get_indexes_dictionary(),
                adaBoostingModel.indexes.get_indexes_dictionary(),
                xgBoostingModel.indexes.get_indexes_dictionary()
            ], columns = ["Random Forest", "ADA Boosting", "XG Boosting"])
        print(indexes)

Runner.ejercicio_4()
