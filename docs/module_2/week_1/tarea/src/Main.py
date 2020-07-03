from utils.Logger import Logger
from utils.ACP import ACP
from utils.ACPPersonalizado import ACPPersonalizado

from data.handler.DataManager import DataManager
from data.graphics.DataVisualizator import DataVisualizator
from data.evaluator.NormalityEvaluator import NormalityEvaluator
from data.evaluator.NumericEvaluator import NumericEvaluator

class Main(Logger):

    # Static properties
    
    # Constructor
    def __init__(self, path, name, alpha = 0.5, debug = False, delimiter = ",", decimal = ".", quotechar = "", columns_to_include = None, colums_to_decode = [], index_col = 0):
        super().__init__(debug)
        self.__data_visualizator = DataVisualizator()
        self.__data_manager = DataManager(path = path, name = name, delimiter = delimiter, decimal = decimal, quotechar = quotechar, columns_to_include = columns_to_include, colums_to_decode = colums_to_decode, index_col = index_col)
        self.__normality_evaluator = NormalityEvaluator(debug, alpha)
        self.__numeric_evaluator = NumericEvaluator(debug = debug, data = self.data_manager.data)
        self.__acp = ACP(self.data_manager.data, n_componentes = 3)

    # Public methods
    def execute_numeric_summary(self):
        self.numeric_evaluator.display_numeric_summary()

    def execute_normality_test(self, variable_1):
        variable_values_1 = self.data_manager.get_column_values(variable_1)
        
        test_saphiro = self.normality_evaluator.test_saphiro_wilk(variable_values_1)
        self.info("Test Saphiro-Wilk:")
        if test_saphiro:
            self.info("La grafica sigue la curva, la muestra proviene de una distribución normal")
        else:
            self.info("La grafica NO sigue la curva, la muestra NO proviene de una distribución normal")
        
        self.info("Test Kolmogorov-Smirnov:")
        test_ks = self.normality_evaluator.test_kolmogorov_smirnov(variable_values_1)
        if test_ks:
            self.info("La grafica sigue la curva, la muestra proviene de una distribución normal")
        else:
            self.info("La grafica NO sigue la curva, la muestra NO proviene de una distribución normal")
        # Drwaw Normality
        self.data_visualizator.draw_plot(variable_values_1)

    def execute_dispercsion_graphic(self, variable_names):
        self.data_visualizator.draw_dispersion(self.data_manager.data, variable_names)

    def execute_show_atipic_data(self, variable_names):
        self.data_visualizator.draw_box_plots(self.data_manager.data, variable_names) 

    def execute_calculation_correlation_matrix(self):
        correlation = self.data_manager.get_correlation_matrix()
        print(correlation)
    
    def execute_draw_correlation_matrix(self):
        correlation = self.data_manager.get_correlation_matrix()
        self.data_visualizator.draw_correlation(correlation)

    def show_correlation_values(self):
        print(self.acp.coordenadas_ind)
        print(self.acp.cos2_ind)
        print(self.acp.correlacion_var)

    def show_correlation_circle(self, ejes = [0, 1]):
        self.acp.plot_circulo()

    def show_correlation_flat(self, ejes = [0, 1]):
        self.acp.plot_plano_principal(ejes = ejes)

    def show_superposition(self, ejes = [0, 1]):
        self.acp.plot_sobreposicion(ejes = ejes)

    def execute_personalized_ACP(self, columns, cos2_min):
        acp_new = ACPPersonalizado(self.data_manager.data, n_componentes = 3, columnas = columns)
        acp_new.plot_plano_principal(cos2_min = cos2_min)
        acp_new.plot_sobreposicion(cos2_min = cos2_min)

    # Private Methods
    
    # Getters and Setters
    @property 
    def data_manager(self):
        return self.__data_manager

    @property 
    def data_visualizator(self):
        return self.__data_visualizator

    @property 
    def normality_evaluator(self):
        return self.__normality_evaluator

    @property 
    def numeric_evaluator(self):
        return self.__numeric_evaluator

    @property
    def acp(self):
        return self.__acp
    
    # Method to override ACP
    @acp.setter
    def acp(self, acp):
        self.__acp = acp


# folder = "/Users/rsalazar/Development/learning/machine_learning/module_2/week_1/homework/resources"
# file3   = "SAheart.csv"
# alpha  = 0.5
# debug  = False
# colums_to_decode = [
#     ["famhist", {"Absent": 0, "Present": 1}],
#     ["chd", {"No": 0, "Si": 1}]
# ]

# main3_2 = Main(path = folder, name = file3, alpha = alpha, debug = debug, delimiter = ";", decimal = ".", colums_to_decode = colums_to_decode, index_col = False)