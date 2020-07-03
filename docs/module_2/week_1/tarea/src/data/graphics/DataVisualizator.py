from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
import seaborn as sns
import numpy as np

class DataVisualizator:
    
    #Constructor
    def __init__(self):
        pass

    # Public Methods
    def draw_plot(self, data):
        qqplot(data, line='s')

    def draw_dispersion(self, data, variable_names):
        sns.pairplot(data, vars = variable_names, height=5)

    def draw_box_plots(self, data, variable_names):
        data.head()
        data.boxplot(column=variable_names,return_type='dict', rot=45)

    def draw_correlation(self, correlation):
        pyplot.subplots(figsize=(13, 13))
        sns.heatmap(correlation, square = True, annot = True, cmap = sns.diverging_palette(150, 275, s=80, l=55, n=9))

    # Private Methods


    # Getters and Setters
    