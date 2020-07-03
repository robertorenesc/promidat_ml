from .GenericModel import GenericModel

from sklearn.tree import DecisionTreeClassifier 

class DecisionTreeModel(GenericModel):

    def __init__(self, data):
        super().__init__(data)

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        criterion = self.read_parameter(metadata, "criterion", "gini")
        min_samples_leaf = self.read_parameter(metadata, "min_samples_leaf", 1)
        min_samples_split = self.read_parameter(metadata, "min_samples_split", 2)
        
        self.classifier_instance = DecisionTreeClassifier(random_state=0, criterion=criterion, min_samples_leaf = min_samples_leaf, min_samples_split=min_samples_split)
        self.classifier_instance.fit(self.X_train,self.y_train.iloc[:,0].values)
        self.prediction = self.classifier_instance.predict(self.X_test)