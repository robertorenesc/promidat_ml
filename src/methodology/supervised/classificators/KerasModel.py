from .GenericModel import GenericModel

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np


class KerasModel(GenericModel):

    def __init__(self, data, binary = True, use_dummy_x = False):
        super().__init__(data)
        self.__binary = True
        self.__use_dummy_x = use_dummy_x
        self.__columns = None

    def build_model(self, variable_predict, train_size = 0.7):
        self.X = self.data.loc[:,self.data.columns != variable_predict]
        self.Y = self.data.loc[:,self.data.columns == variable_predict]

        # Prepare X data
        scaler = MinMaxScaler(feature_range=(0, 1))
        if self.__use_dummy_x:
            self.X = pd.get_dummies(self.X)
        scaled_X  = pd.DataFrame(scaler.fit_transform(self.X), columns = list(self.X))

        # Prepare Y data
        if self.__binary:
            dummy_y = pd.get_dummies(self.Y, prefix = "", prefix_sep="")
            self.Y = pd.DataFrame(dummy_y[dummy_y.columns[0]], columns=[dummy_y.columns[0]])
            self.__columns = dummy_y.columns
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(scaled_X, self.Y, train_size = train_size, random_state = 0)

    def __prepare_binary_model(self, input_dim):
        # Setting layers using sigmoid
        self.classifier_instance.add(Dense(10, input_dim = input_dim, activation = "relu"))
        self.classifier_instance.add(Dense(10, activation = "relu"))
        self.classifier_instance.add(Dense(10, activation = "relu"))
        self.classifier_instance.add(Dense(5, activation = "sigmoid"))
        self.classifier_instance.add(Dense(1, activation = "sigmoid"))

    def __prepare_non_binary_model(self, input_dim):
        self.classifier_instance.add(Dense(10, input_dim = input_dim, activation = "relu"))
        self.classifier_instance.add(Dense(10, activation = "relu"))
        self.classifier_instance.add(Dense(10, activation = "relu"))
        self.classifier_instance.add(Dense(5, activation = "softmax"))

    def prepare_model(self, layers:list, input_dim:int = 4,optimizer = "adam", metrics = ["accuracy"]):
        self.classifier_instance = Sequential()
        if self.__binary:
            self.__prepare_binary_model(input_dim)
            self.classifier_instance.compile(loss = "binary_crossentropy", optimizer = optimizer, metrics = metrics)
        else:
            self.__prepare_non_binary_model(input_dim)
            self.classifier_instance.compile(loss = "category_crossentropy", optimizer = optimizer, metrics = metrics)
        print(self.classifier_instance.summary())

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        layers = self.read_parameter(metadata, parameter = "layers", default = None)
        input_dim = self.read_parameter(metadata, parameter = "input_dim", default = 4)
        optimizer = self.read_parameter(metadata, parameter = "optimizer", default = "adam")
        metrics = self.read_parameter(metadata, parameter = "metrics", default = ["accuracy"])

        # Preparing the model to predict
        input_dim = len(self.X_train.columns)
        self.prepare_model(layers = layers, input_dim = input_dim, optimizer = optimizer, metrics = metrics)

        # Prediction process
        self.classifier_instance.fit(self.X_train,self.y_train.iloc[:,0].values, epochs = 100, batch_size = 50, verbose = 0)
        pred = self.classifier_instance.predict(self.X_test)
        y_pred = np.round(pred)
        # Convertimos a columna
        #y_test_class = np.argmax(np.asanyarray(self.y_test), axis = 1)  # Convertimos a array
        #y_pred_class = np.argmax(y_pred, axis = 1)

        scores = self.classifier_instance.evaluate(self.X_test, self.y_test)
        self.create_confusion_matrix(self.y_test, y_pred, self.__columns)