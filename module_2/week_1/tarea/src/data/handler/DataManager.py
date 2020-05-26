import pandas as pandas
import os

class DataManager:

    #Constructor
    def __init__(self, path = "", name = "", delimiter = ",", decimal = ".", quotechar = "", columns_to_include = None, colums_to_decode = [], index_col = 0):
        self.__path = path
        self.__name = name
        self.__data = self.__read_csv(delimiter, decimal, quotechar, index_col)
        if columns_to_include != None:
            self.data = self.data[columns_to_include]
        for column in colums_to_decode:
            self.decode_column(column[0], column[1])
        
    # Public Methods
    def print_data(self):
        print(self.data.head())
        print(self.data.shape)

    def get_column_values(self, column_name):
        return self.data[column_name].values

    def get_correlation_matrix(self):
        return self.data.corr()

    def get_max_column_value(self, column_name):
        return self.data[column_name].max()

    def decode_column(self, column_name, codes):
        self.data[column_name] = self.__recodificar(self.data[column_name], codes)
    

    # Private Methods
    def __read_csv(self, delimiter = ',', decimal = ".", quotechar = "", index_col = 0):
        os.chdir(self.path)
        if quotechar == "":
            return pandas.read_csv(self.name, delimiter = delimiter, decimal = decimal, index_col = index_col)
        else:
            return pandas.read_csv(self.name, delimiter = delimiter, decimal = decimal, quotechar = quotechar, index_col=index_col)

    def __recodificar(self, col, nuevo_codigo):
        col_cod = pandas.Series(col, copy=True)
        for llave, valor in nuevo_codigo.items():
            col_cod.replace(llave, valor, inplace=True)
        return col_cod

    # Getters and Setters
    @property 
    def path(self):
        return self.__path

    @property 
    def name(self):
        return self.__name

    @property 
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

