from Vuelo import Vuelo

class VueloCarga(Vuelo):

    # Constructor
    def __init__(self):
        super().__init__()
        self.__peso_maximo = 0.0

    # Public Methods
    def captura(self):
        super().captura()
        self.peso_maximo = float(input("Peso maximo: "))

    def __str__(self):
        return "%s" \
               "  \t- Peso maximo: %s\n%s" \
               % (str(super().__str__()), self.peso_maximo, self.DOUBLE_LINE_SEPARATOR)

    # Setters and Getters
    @property
    def peso_maximo(self):
        return self.__peso_maximo

    @peso_maximo.setter
    def peso_maximo(self, peso_maximo):
        self.__peso_maximo = peso_maximo