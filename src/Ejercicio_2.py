from utils.DataFrameUtils import DataFrameUtils
from methodology.supervised.classificators.MLPerceptronModel import MLPerceptronModel
from methodology.supervised.classificators.KNeighborsModel import KNeighborsModel
from methodology.supervised.classificators.ADABoostingModel import ADABoostingModel
from methodology.supervised.classificators.XGBoostingModel import XGBoostingModel
from methodology.supervised.classificators.RandomForestModel import RandomForestModel
from methodology.supervised.classificators.SVMModel import SVMModel
from methodology.supervised.classificators.DecisionTreeModel import DecisionTreeModel
from methodology.supervised.classificators.KerasModel import KerasModel


tumores_path = "/Users/rsalazar/Development/learning/machine_learning/promidat/src/data/tumores.csv"
data_tumores = DataFrameUtils.read_cvs(tumores_path, delimiter=",", decimal=".", index_col=0)
data_tumores['tipo'] = data_tumores['tipo'].astype('category')
print(data_tumores)

# 1. Utilizando el modelo MLPClassifier
mlpModel = MLPerceptronModel(data_tumores)
mlpModel.build_model(variable_predict="tipo", train_size=0.7)
mlpModel.print_testing_info()
mlpModel.train_model(metadata = {"hidden_layer_sizes": (1000,500)})
mlpModel.print_indexes_info()

# 1. Utilizando el modelo Tensorflow/Keras

kerasModel = KerasModel(data_tumores)
kerasModel.build_model(variable_predict = "tipo", train_size = 0.7)
kerasModel.print_testing_info()
kerasModel.train_model(metadata={})
kerasModel.print_indexes_info()

# 2.  Generación de los modelos anteriores

# K-Neighbors
kNeighborsModel = KNeighborsModel(data_tumores)
kNeighborsModel.build_model(variable_predict = "tipo", train_size = 0.7)
kNeighborsModel.train_model(metadata = {})
kNeighborsModel.calculate_indexes()

# Random Forest
randomForestModel = RandomForestModel(data_tumores)
randomForestModel.build_model(variable_predict = "tipo", train_size = 0.7)
randomForestModel.train_model(metadata = {})
randomForestModel.calculate_indexes()

# ADA Boosting
adaBoostingModel = ADABoostingModel(data_tumores)
adaBoostingModel.build_model(variable_predict = "tipo", train_size = 0.7)
adaBoostingModel.train_model(metadata = {})
adaBoostingModel.calculate_indexes()

# ADA Boosting
xgBoostingModel = XGBoostingModel(data_tumores)
xgBoostingModel.build_model(variable_predict = "tipo", train_size = 0.7)
xgBoostingModel.train_model(metadata = {})
xgBoostingModel.calculate_indexes()

# Decision Tree
decisionTreeModel = DecisionTreeModel(data_tumores)
decisionTreeModel.build_model(variable_predict = "tipo", train_size = 0.7)
decisionTreeModel.train_model(metadata = {})
decisionTreeModel.calculate_indexes()

# Support Vector Machines
svmModel = SVMModel(data_tumores)
svmModel.build_model(variable_predict = "tipo", train_size = 0.7)
svmModel.train_model(metadata = {})
svmModel.calculate_indexes()

# 3. Generación de cuadro comparativo
print("Matriz de Comparación")
indexes = DataFrameUtils.create_dataframe_from_dict(
    [
        kNeighborsModel.indexes.get_indexes_dictionary(),
        randomForestModel.indexes.get_indexes_dictionary(),
        adaBoostingModel.indexes.get_indexes_dictionary(),
        xgBoostingModel.indexes.get_indexes_dictionary(),
        svmModel.indexes.get_indexes_dictionary(),
        decisionTreeModel.indexes.get_indexes_dictionary(),
        mlpModel.indexes.get_indexes_dictionary(),
        kerasModel.indexes.get_indexes_dictionary()
    ], columns = [
        "K-Neighbors",
        "Random Forest", 
        "ADA Boosting", 
        "XG Boosting",
        "SVM Model",
        "Decision Tree",
        "Multi Layer Perceptron",
        "Tensorflow/Keras"])
print(indexes)
