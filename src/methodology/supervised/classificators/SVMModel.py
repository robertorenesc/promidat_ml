from .GenericModel import GenericModel

from sklearn.svm import SVC

class SVMModel(GenericModel):

    def __init__(self, data):
        super().__init__(data)

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        kernel = self.read_parameter(metadata, "kernel", "rbf")
        
        self.classifier_instance = SVC(kernel = kernel)
        self.classifier_instance.fit(self.X_train,self.y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.X_test)