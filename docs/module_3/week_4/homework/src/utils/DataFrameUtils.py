import pandas as pd
import numpy as np

class DataFrameUtils:

    @staticmethod
    def create_dataframe(matrix, indexes = None, columns = None):
        data_frame = None
        data_frame = pd.DataFrame(matrix, columns = columns, index = indexes)
        return data_frame

    @staticmethod
    def create_dataframe_from_dict(dictionaries = [], columns = []):
        data_frame = pd.DataFrame(dictionaries)
        if len(columns) > 0:
            data_frame = data_frame.T
            data_frame.columns = columns
        return data_frame
    
    @staticmethod
    def filter_columns(data_frame, columns_to_use = None):
        if columns_to_use == None:
            return data_frame
        return data_frame[columns_to_use]
    
    @staticmethod
    def filter_rows(data_frame, column:str, allowed_values:list):
        is_allowed_value = data_frame[column].isin(allowed_values)
        return data_frame.loc[is_allowed_value]

    @staticmethod
    def read_cvs(path, delimiter = ";", decimal = ".", index_col = 0):
        data_frame = pd.read_csv(path, delimiter = delimiter, decimal = decimal, index_col = index_col)
        return data_frame
    
    @staticmethod
    def change_column_type(data_frame, column_name, type):
        data_frame[column_name] = data_frame[column_name].astype(type)

    @staticmethod
    def recode_category(data_frame, column_name):
        data_frame[column_name] = data_frame.cat.codes
        DataFrameUtils.change_column_type(data_frame, column_name, "category")

    @staticmethod
    def array_to_matrix(array, matrix_size):
        step = 0
        matrix = []
        element = []
        for i in range(matrix_size**2):
            element.append(array[i])
            step = step + 1
            if step == matrix_size:
                matrix.append(element)
                step = 0
                element = []
        return np.array(matrix)

    @staticmethod
    def sub_matrices(matrix, matrix_size, dimension):
        matrices = []
        for x in range(0, matrix_size, dimension):
            for y in range(0, matrix_size, dimension):
                matrices.append(matrix[x:x+dimension,y:y+dimension])
        return matrices

    @staticmethod
    def average_by_submatrix(array, matrix_size, dimension):
        matrix = DataFrameUtils.array_to_matrix(array, matrix_size)
        matrices = DataFrameUtils.sub_matrices(matrix, matrix_size, dimension)
        return [m.mean() for m in matrices]

    @staticmethod
    def replace_all_by_average(data_frame, var_predict, matrix_size = 16, dimension = 4):
        data_replace = data_frame.loc[:, data_frame.columns != var_predict]
        data_test = data_frame.loc[:, data_frame.columns == var_predict]
        data_mtx = data_replace.to_numpy()
        averages = []
        #print(DataFrameUtils.average_by_submatrix(data_mtx[0], matrix_size, dimension))
        for line in data_mtx:
            averages.append(DataFrameUtils.average_by_submatrix(line, matrix_size, dimension))
        cols = [f"Avg_{i+1}" for i in range(int((matrix_size/dimension)**2))]
        df_averages = DataFrameUtils.create_dataframe(np.array(averages), columns=cols)
        return pd.concat([data_test, df_averages], axis = 1)