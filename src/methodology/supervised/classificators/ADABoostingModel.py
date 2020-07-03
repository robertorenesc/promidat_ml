from .GenericModel import GenericModel

from sklearn.ensemble import AdaBoostClassifier
import matplotlib.pyplot as plt
import numpy  as np

class ADABoostingModel(GenericModel):

    def __init__(self, data):
        super().__init__(data)

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        algorithm = self.read_parameter(metadata, "algorithm", "SAMME.R")
        n_estimators = self.read_parameter(metadata, "n_estimators", 50)
        
        self.classifier_instance = AdaBoostClassifier(algorithm=algorithm, n_estimators=n_estimators, random_state=0)
        self.classifier_instance.fit(self.X_train,self.y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.X_test)

    def plot_prediction(self):
        pass