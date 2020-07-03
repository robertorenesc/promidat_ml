from .GenericModel import GenericModel

from sklearn.neural_network import MLPClassifier 

class MLPerceptronModel(GenericModel):

    def __init__(self, data):
        super().__init__(data)

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        solver = self.read_parameter(metadata, parameter = "solver", default = "adam")
        hidden_layer_sizes = self.read_parameter(metadata, parameter = "hidden_layer_sizes", default = (100,))
        
        self.classifier_instance = MLPClassifier(random_state=0, solver=solver, hidden_layer_sizes = hidden_layer_sizes)
        self.classifier_instance.fit(self.X_train,self.y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.X_test)