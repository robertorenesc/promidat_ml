from utils.Logger import Logger

class NumericEvaluator(Logger):

    # Constructor
    def __init__(self, debug = False, data = None):
        super().__init__(debug)
        self.__data = data

    def display_numeric_summary(self):
        self.info(self.data.dropna().describe())
        self.info(self.data.describe())
        self.info(self.data.mean(numeric_only=True))
        self.info(self.data.median(numeric_only=True))
        self.info(self.data.std(numeric_only=True))
        self.info(self.data.max(numeric_only=True))

    @property 
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data