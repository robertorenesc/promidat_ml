from IndexesCalculator import IndexesCalculator
from DataFrameUtils import DataFrameUtils

matrix = [[892254, 212],
          [8993,   300]]
confusion_matrix = DataFrameUtils.create_dataframe(matrix, indexes = ["NO", "SI"], columns = ["NO", "SI"])
calculator = IndexesCalculator(confusion_matrix)
calculator.show_confusion_matrix_indexes()
