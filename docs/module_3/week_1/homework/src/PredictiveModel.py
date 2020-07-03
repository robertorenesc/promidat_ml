
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from DataFrameUtils import DataFrameUtils
from pandas import DataFrame

class PredictiveModel:
    
    # Constructor
    def __init__(self, data = None):
        self.__data = data
        self.__X = None
        self.__Y = None
        self.__train_size = None
        self.__n_neighbors = None
        self.__knn_instance = None
        self.__confusion_matrix = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def build_model(self, variable_predict, train_size = 0.7):
        print("Variables Predictoras:")
        self.X = self.data.loc[:,self.data.columns != variable_predict]
        print(self.X.head())

        print("Variable a Predecir:")
        self.Y = self.data.loc[:,self.data.columns == variable_predict]
        print(self.Y.head())
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, train_size = train_size, random_state=0)

    def build_model_with_data(self, variable_predict, train_df: DataFrame, test_df: DataFrame, n_neighbors = 5, algorithm = "auto"):
        self.X_train = train_df.loc[:, train_df.columns != variable_predict]
        self.X_test = test_df.loc[:, test_df.columns != variable_predict]
        self.y_train = train_df.loc[:,train_df.columns == variable_predict]
        self.y_test = test_df.loc[:,test_df.columns == variable_predict]

    def train_model(self, n_neighbors = 5, algorithm = "auto"):
        self.knn_instance = KNeighborsClassifier(n_neighbors = n_neighbors, algorithm = algorithm, p = 3)
        self.knn_instance.fit(self.X_train,self.y_train.iloc[:,0].values)
        print("Las predicciones en Testing son: {}".format(self.knn_instance.predict(self.X_test)))

    def obtain_confusion_matrix(self):
        if self.knn_instance == None:
            print("Se debe inicializar el modelo para poder obtener la matriz de confusión")
            return None
        prediccion = self.knn_instance.predict(self.X_test)
        self.confusion_matrix = confusion_matrix(self.y_test, prediccion)
        return DataFrameUtils.create_dataframe(self.confusion_matrix, indexes=self.knn_instance.classes_, columns=self.knn_instance.classes_)

    @property 
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property 
    def X(self):
        return self.__X
    
    @X.setter
    def X(self, X):
        self.__X = X

    @property 
    def Y(self):
        return self.__Y
    
    @Y.setter
    def Y(self, Y):
        self.__Y = Y

    @property 
    def train_size(self):
        return self.__train_size
    
    @train_size.setter
    def train_size(self, train_size):
        self.__train_size = train_size

    @property 
    def n_neighbors(self):
        return self.__n_neighbors
    
    @n_neighbors.setter
    def n_neighbors(self, n_neighbors):
        self.__n_neighbors = n_neighbors
    
    @property 
    def knn_instance(self):
        return self.__knn_instance
    
    @knn_instance.setter
    def knn_instance(self, knn_instance):
        self.__knn_instance = knn_instance

    @property 
    def confusion_matrix(self):
        return self.__confusion_matrix
    
    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        self.__confusion_matrix = confusion_matrix