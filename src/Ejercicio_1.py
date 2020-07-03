from utils.DataFrameUtils import DataFrameUtils
from methodology.supervised.classificators.MLPerceptronModel import MLPerceptronModel
from methodology.supervised.classificators.KNeighborsModel import KNeighborsModel
from methodology.supervised.classificators.ADABoostingModel import ADABoostingModel
from methodology.supervised.classificators.XGBoostingModel import XGBoostingModel
from methodology.supervised.classificators.RandomForestModel import RandomForestModel
from methodology.supervised.classificators.SVMModel import SVMModel
from methodology.supervised.classificators.DecisionTreeModel import DecisionTreeModel
from methodology.supervised.classificators.KerasModel import KerasModel

# 1. 
voces_path = "/Users/rsalazar/Development/learning/machine_learning/promidat/src/data/voces.csv"
data_voces = DataFrameUtils.read_cvs(voces_path, delimiter=",", decimal=".", index_col=None)
print(data_voces)

# 2.
mlpModel = MLPerceptronModel(data_voces)
mlpModel.build_model(variable_predict="genero", train_size=0.2)
mlpModel.print_testing_info()

# 3.
mlpModel.train_model(metadata = {"hidden_layer_sizes": (1000,500)})

# 4.
mlpModel.print_indexes_info()

# 5.1. Generación de los modelos anteriores
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

# Decision Tree
decisionTreeModel = DecisionTreeModel(data_voces)
decisionTreeModel.build_model(variable_predict = "genero", train_size = 0.8)
decisionTreeModel.train_model(metadata = {})
decisionTreeModel.calculate_indexes()

# Support Vector Machines
svmModel = SVMModel(data_voces)
svmModel.build_model(variable_predict = "genero", train_size = 0.8)
svmModel.train_model(metadata = {})
svmModel.calculate_indexes()

# 5.2 Generación de cuadro comparativo
print("Matriz de Comparación")
indexes = DataFrameUtils.create_dataframe_from_dict(
    [
        kNeighborsModel.indexes.get_indexes_dictionary(),
        randomForestModel.indexes.get_indexes_dictionary(),
        adaBoostingModel.indexes.get_indexes_dictionary(),
        xgBoostingModel.indexes.get_indexes_dictionary(),
        svmModel.indexes.get_indexes_dictionary(),
        decisionTreeModel.indexes.get_indexes_dictionary(),
        mlpModel.indexes.get_indexes_dictionary()
    ], columns = [
        "K-Neighbors",
        "Random Forest", 
        "ADA Boosting", 
        "XG Boosting",
        "SVM Model",
        "Decision Tree",
        "Multi Layer Perceptron"])
print(indexes)

# 6. Generación con Tensorflow/Keras

kerasModel = KerasModel(data_voces)
kerasModel.build_model(variable_predict = "genero", train_size = 0.8)
kerasModel.train_model(metadata={})
kerasModel.print_indexes_info()

# 7. Comparación con los resultados anteriores
indexes["Tensorflow/Keras"] = list(kerasModel.indexes.get_indexes_dictionary().values())
print(indexes)