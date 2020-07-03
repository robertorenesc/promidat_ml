from VueloComercial import VueloComercial

class VueloLocal(VueloComercial):

    # Constructor
    def __init__(self):
        super().__init__()
        self.__minimo_pasajeros = 0

    # Public Methods
    def captura(self):
        super().captura()
        self.minimo_pasajeros = int(input("Minimo de pasajeros: "))
        i = 1
        while i <= self.minimo_pasajeros:
            print("\nIngreso de pasajero (%i de %i)" % (i, self.minimo_pasajeros))
            self.agregar_pasajero()
            i += 1
        self.agregar_pasajeros()

    def __str__(self):
        return "%s" \
               " \t- Vuelo Local\n" \
               " \t- Minimo de Pasajeros: %s\n" \
               " \t- Valor recaudado:     %.2f\n%s" \
               % (str(super().__str__()), self.minimo_pasajeros, self.monto_total_vendido(), self.DOUBLE_LINE_SEPARATOR)

    # Setters and Getters
    @property
    def minimo_pasajeros(self):
        return self.__minimo_pasajeros

    @minimo_pasajeros.setter
    def minimo_pasajeros(self, minimo_pasajeros):
        self.__minimo_pasajeros = minimo_pasajeros