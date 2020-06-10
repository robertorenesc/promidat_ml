from GenericModel import GenericModel

from sklearn.neighbors import KNeighborsClassifier

class KNeighborsModel(GenericModel):

    def __init__(self, data):
        super.__init__(data)

    def train_model(self, methadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        n_neighbors = 5 if methadata["n_neighbors"] is None else methadata["n_neighbors"]
        algorithm = "auto" if methadata["algorithm"] is None else methadata["algorithm"]
        self.classifier_instance = KNeighborsClassifier(n_neighbors = n_neighbors, algorithm = algorithm, p = 3)
        self.classifier_instance.fit(self.__X_train, self.__y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.__X_test)