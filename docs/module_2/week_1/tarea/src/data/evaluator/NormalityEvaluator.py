import scipy.stats as stats
import numpy as np

from utils.Logger import Logger

class NormalityEvaluator(Logger):

    # Constructor
    def __init__(self, debug = False, alpha = 0.5):
        super().__init__(debug)
        self.__alpha = alpha

    # Public Methods
    def test_saphiro_wilk(self, data_array):
        self.debug(data_array.shape)
        shapiro_result = stats.shapiro(data_array)
        self.debug(shapiro_result)
        p_value = shapiro_result[1]
        self.debug(p_value)
        return p_value > self.alpha

    def test_kolmogorov_smirnov(self, data_array):
        self.debug(data_array.shape)
        ks_results = stats.kstest(data_array, cdf='norm')
        self.debug(ks_results)
        p_value = ks_results[1]
        self.debug(p_value)
        return p_value > self.alpha

    # Getters and Setters
    @property 
    def alpha(self):
        return self.__alpha

