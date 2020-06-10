from GenericModel import GenericModel

from sklearn.ensemble import AdaBoostClassifier
import matplotlib.pyplot as plt
import numpy  as np

class KNeighborsModel(GenericModel):

    def __init__(self, data):
        super.__init__(data)

    def train_model(self, methadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        algorithm = "SAMME.R" if methadata["algorithm"] is None else methadata["algorithm"]
        n_estimators = 50 if methadata["n_estimators"] is None else methadata["n_estimators"]
        
        self.classifier_instance = AdaBoostClassifier(algorithm=algorithm, n_estimators=n_estimators, random_state=0)
        self.classifier_instance.fit(self.__X_train,self.__y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.__X_test)

    def plot_prediction(self):
        importance = self.classifier_instance.feature_importances_
        labels = self.__X_train.columns.values
        y_pos = np.arange(len(labels))
        plt.barh(y_pos, importance, align='center', alpha=0.5)
        plt.yticks(y_pos, labels)