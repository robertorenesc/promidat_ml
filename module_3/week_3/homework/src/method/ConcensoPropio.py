from pandas import DataFrame

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

class ConcensoPropio:

    def __init__(self):
        self.__kn_classifier = None
        self.__dec_tree_classifier = None
        self.__ada_classifier = None
        self.__xg_classifier = None
        self.__models = None
        self.__init_models()
    
    def __init_models(self):
        self.kn_classifier = KNeighborsClassifier()
        self.dec_tree_classifier = DecisionTreeClassifier()
        self.ada_classifier = AdaBoostClassifier()
        self.xg_classifier = GradientBoostingClassifier()
        self.__models = DataFrame(
            [
                self.kn_classifier, 
                self.dec_tree_classifier, 
                self.ada_classifier, 
                self.xg_classifier 
            ],
            columns = ["Modelos"])
        print(self.__models)

    def fit(self, X_train, y_train):
        self.__models.apply(lambda model: model[0].fit(X_train, y_train.iloc[:,0].values))
        # self.kn_classifier.fit(X_train, y_train.iloc[:,0].values)
        # self.dec_tree_classifier.fit(X_train, y_train)
        # self.ada_classifier.fit(X_train,y_train.iloc[:,0].values)
        # self.xg_classifier.fit(X_train,y_train.iloc[:,0].values)

    def predict(self):
        #self.prediction = self.classifier_instance.predict(self.__X_test)
        pass

    @property
    def kn_classifier(self):
        return self.__kn_classifier
    
    @kn_classifier.setter
    def kn_classifier(self, kn_classifier):
        self.__kn_classifier = kn_classifier

    @property
    def dec_tree_classifier(self):
        return self.__dec_tree_classifier
    
    @dec_tree_classifier.setter
    def dec_tree_classifier(self, dec_tree_classifier):
        self.__dec_tree_classifier = dec_tree_classifier
    
    @property
    def ada_classifier(self):
        return self.__ada_classifier
    
    @ada_classifier.setter
    def ada_classifier(self, ada_classifier):
        self.__ada_classifier = ada_classifier

    @property
    def xg_classifier(self):
        return self.__xg_classifier
    
    @xg_classifier.setter
    def xg_classifier(self, xg_classifier):
        self.__xg_classifier = xg_classifier