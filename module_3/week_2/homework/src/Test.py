from DataFrameUtils import DataFrameUtils

data2 = DataFrameUtils.read_cvs("/Users/rsalazar/Development/learning/machine_learning/Promidat/module_3/week_2/homework/src/data/voces.csv", delimiter = ",", index_col = None)
print(data2.head())

from PredictiveModel import PredictiveModel

predictiveModel2 = PredictiveModel(data2)
predictiveModel2.build_model("genero", train_size = 0.8)
predictiveModel2.train_model()

confusion_matrix2 = predictiveModel2.obtain_confusion_matrix()
print(f"Matriz de confusión:\n{confusion_matrix2}")

from IndexesCalculator import IndexesCalculator

calculator2 = IndexesCalculator(confusion_matrix2)
print(f"Precisión Global: \n{calculator2.accurancy}\n")
print(f"Precision por Categoría: \n{calculator2.category_precisions}\n")

rows1 = calculator2.get_indexes_dictionary()
import matplotlib.pyplot as plt
plt.figure(figsize=(16,15))
predictiveModel2.plot_tree()