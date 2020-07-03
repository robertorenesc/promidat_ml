from Base import Base

class Vuelo(Base):

    # Constructor
    def __init__(self):
        self.__numero = 0
        self.__hora_salida = 0
        self.__hora_llegada = 0

    # Public methods
    def captura(self):
        print("\nDatos del Vuelo")
        print("-----------------------------------------")
        self.numero = int(input("Numero: "))
        self.hora_salida = int(input("Hora de Salida: "))
        self.hora_llegada = int(input("Hora de Llegada: "))

    def __str__(self):
        return "  VUELO %i\n%s\n" \
               " \t- Hora de Salida: %i\n" \
               " \t- Hora de Llegada: %i\n" \
               % (self.numero, self.DOUBLE_LINE_SEPARATOR, self.hora_salida, self.hora_llegada)

    # Setters and Getters
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def hora_salida(self):
        return self.__hora_salida

    @hora_salida.setter
    def hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida

    @property
    def hora_llegada(self):
        return self.__hora_llegada

    @hora_llegada.setter
    def hora_llegada(self, hora_llegada):
        self.__hora_llegada = hora_llegada

