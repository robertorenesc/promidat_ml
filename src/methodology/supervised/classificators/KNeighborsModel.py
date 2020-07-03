from .GenericModel import GenericModel

from sklearn.neighbors import KNeighborsClassifier

class KNeighborsModel(GenericModel):

    def __init__(self, data):
        super().__init__(data)

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")

        n_neighbors = self.read_parameter(metadata, "n_neighbors", 5)
        algorithm = self.read_parameter(metadata, "algorithm", "auto")

        self.classifier_instance = KNeighborsClassifier(n_neighbors = n_neighbors, algorithm = algorithm, p = 3)
        self.classifier_instance.fit(self.X_train, self.y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.X_test)
