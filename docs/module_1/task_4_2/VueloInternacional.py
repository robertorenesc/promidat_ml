from VueloComercial import VueloComercial

class VueloInternacional(VueloComercial):

    # Constructor
    def __init__(self):
        super().__init__()
        self.__pais_destino = ""

    # Public Methods
    def captura(self):
        super().captura()
        self.pais_destino = input("Pais: ")
        self.agregar_pasajeros()
        
    def __str__(self):
        return "%s" \
               " \t- Vuelo Internacional\n" \
               " \t- Pais:            %s\n" \
               " \t- Valor recaudado: %.2f\n%s" \
               % (str(super().__str__()), self.pais_destino, self.monto_total_vendido(), self.DOUBLE_LINE_SEPARATOR)    

    # Setters and Getters
    @property
    def pais_destino(self):
        return self.__pais_destino

    @pais_destino.setter
    def pais_destino(self, pais_destino):
        self.__pais_destino = pais_destino