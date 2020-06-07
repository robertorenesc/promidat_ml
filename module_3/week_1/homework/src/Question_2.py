from IndexesCalculator import IndexesCalculator
from DataFrameUtils import DataFrameUtils
from PredictiveModel import PredictiveModel

# data = DataFrameUtils.read_cvs("/Users/rsalazar/Development/learning/machine_learning/Promidat/module_3/week_1/homework/src/data/voces.csv", delimiter = ",", index_col = None)
# print(data.head())


# predictiveModel = PredictiveModel(data)
# predictiveModel.build_model("genero")
# predictiveModel.train_model(train_size = 0.8)
# confusion_matrix = predictiveModel.obtain_confusion_matrix()

# # calculator2 = IndexesCalculator(confusion_matrix)
# # #calculator2.show_confusion_matrix_indexes()
# # rows = calculator2.get_indexes_dictionary()
# # print(rows)

# data_train = DataFrameUtils.read_cvs("/Users/rsalazar/Development/learning/machine_learning/Promidat/module_3/week_1/homework/src/data/ZipDataTrainCod.csv", index_col = None)
# print(data_train.head())

# data_test = DataFrameUtils.read_cvs("/Users/rsalazar/Development/learning/machine_learning/Promidat/module_3/week_1/homework/src/data/ZipDataTestCod.csv", index_col = None)
# print(data_test.head())

# predictiveModel = PredictiveModel()
# predictiveModel.build_model_with_data("Numero", data_train, data_test)

# predictiveModel.train_model()

# confusion_matrix = predictiveModel.obtain_confusion_matrix()
# calculator = IndexesCalculator(confusion_matrix)
# indexes = calculator.get_indexes_dictionary()
# print(indexes)


import numpy as np

#data_test = DataFrameUtils.read_cvs("/Users/rsalazar/Development/learning/machine_learning/Promidat/module_3/week_1/homework/src/data/ZipDataTestCod.csv", index_col = None)
#data_test = DataFrameUtils.filter_rows(data_test, "Numero", ["tres", "cinco", "ocho"])
#data_test = DataFrameUtils.replace_all_by_average(data_test, "Numero", 16, 4)
data_train = DataFrameUtils.read_cvs("/Users/rsalazar/Development/learning/machine_learning/Promidat/module_3/week_1/homework/src/data/ZipDataTrainCod.csv", index_col = None)
data_train = DataFrameUtils.replace_all_by_average(data_train, "Numero", 16, 16)

#print(data_test)
print(data_train)