
from sklearn.model_selection import train_test_split
from sklearn import tree 
from sklearn.metrics import confusion_matrix
from DataFrameUtils import DataFrameUtils
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import graphviz

class PredictiveModel:
    
    # Constructor
    def __init__(self, data = None):
        self.__data = data
        self.__X = None
        self.__Y = None
        self.__train_size = None
        self.__n_neighbors = None
        self.__tree_instance = None
        self.__confusion_matrix = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def build_model(self, variable_predict, train_size = 0.7):
        print("Variables Predictoras:")
        self.X = self.data.loc[:,self.data.columns != variable_predict]
        print(self.X.head())
        print("\n")
        print("Variable a Predecir:")
        self.Y = self.data.loc[:,self.data.columns == variable_predict]
        print(self.Y.head())
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, train_size = train_size, random_state=0)
        print("\n")

    def build_model_with_data(self, variable_predict, train_df: DataFrame, test_df: DataFrame, algorithm = "auto"):
        self.X_train = train_df.loc[:, train_df.columns != variable_predict]
        self.X_test = test_df.loc[:, test_df.columns != variable_predict]
        self.y_train = train_df.loc[:,train_df.columns == variable_predict]
        self.y_test = test_df.loc[:,test_df.columns == variable_predict]

    def train_model(self, criterion = "gini", min_samples_leaf = 1, min_samples_split = 2):
        self.tree_instance = tree.DecisionTreeClassifier(random_state=0, criterion=criterion, min_samples_leaf = min_samples_leaf, min_samples_split=min_samples_split)
        self.tree_instance.fit(self.X_train,self.y_train)
        print("Las predicciones en Testing son:\n{}".format(self.tree_instance.predict(self.X_test)))
        print("\n")

    def obtain_confusion_matrix(self):
        if self.tree_instance == None:
            print("Se debe inicializar el modelo para poder obtener la matriz de confusión")
            return None
        prediccion = self.tree_instance.predict(self.X_test)
        self.confusion_matrix = confusion_matrix(self.y_test, prediccion)
        return DataFrameUtils.create_dataframe(self.confusion_matrix, indexes=self.tree_instance.classes_, columns=self.tree_instance.classes_)

    def plot_tree_easy(self):
        plt.figure(figsize=(16,15))
        tree.plot_tree(self.tree_instance.fit(self.X_train,self.y_train), class_names=self.tree_instance.classes_, filled=True)

    def plot_tree(self):
        plt.figure(figsize=(16,15))
        dot_data = tree.export_graphviz(self.tree_instance.fit(self.X_train,self.y_train), out_file=None) 
        graph = graphviz.Source(dot_data) 
        graph.format = "png"
        graphic_file = graph.render()
        img = mpimg.imread(graphic_file)
        plt.imshow(img)
        plt.axis('off')

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
    def tree_instance(self):
        return self.__tree_instance
    
    @tree_instance.setter
    def tree_instance(self, tree_instance):
        self.__tree_instance = tree_instance

    @property 
    def confusion_matrix(self):
        return self.__confusion_matrix
    
    @confusion_matrix.setter
    def confusion_matrix(self, confusion_matrix):
        self.__confusion_matrix = confusion_matrix