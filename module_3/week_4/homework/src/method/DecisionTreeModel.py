from method.GenericModel import GenericModel

from sklearn.tree import DecisionTreeClassifier 

class DecisionTreeModel(GenericModel):

    def __init__(self, data):
        super().__init__(data)

    def train_model(self, metadata: dict):
        if self.X is None or  self.Y is None:
            raise Exception("The model should be built before training")
        
        # Reading the parameters from the dictionary
        criterion = "gini" if metadata["criterion"] is None else metadata["criterion"]
        min_samples_leaf = 1 if metadata["min_samples_leaf"] is None else metadata["min_samples_leaf"]
        min_samples_split = 2 if metadata["min_samples_split"] is None else metadata["min_samples_split"]
        
        self.classifier_instance = DecisionTreeClassifier(random_state=0, criterion=criterion, min_samples_leaf = min_samples_leaf, min_samples_split=min_samples_split)
        self.classifier_instance.fit(self.__X_train,self.__y_train)
        self.prediction = self.classifier_instance.predict(self.__X_test)