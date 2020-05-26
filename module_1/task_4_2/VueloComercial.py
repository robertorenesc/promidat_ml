from Vuelo import Vuelo
from Frecuente import Frecuente
from Pasajero import Pasajero

class VueloComercial(Vuelo):

    # Constructor
    def __init__(self):
        super().__init__()
        self.__pasajeros = []

    # Public methods
    def monto_total_vendido(self):
        monto_total = 0.0
        for i in range(len(self.pasajeros)):
            monto_total += self.pasajeros[i].total_pagar()
        return monto_total

    def captura(self):
        super().captura()

    def __str__(self):
        text = str(super().__str__())
        text += self.LINE_SEPARATOR
        for i in range(len(self.pasajeros)):
            text += str(self.pasajeros[i])
        text += self.LINE_SEPARATOR
        return text

    def agregar_pasajeros(self):
        option = ""
        while option != "n":
            option = input("\nDesea agregar un nuevo pasajero al vuelo? (y/n): ")
            if option == "y":
                self.agregar_pasajero()

    def agregar_pasajero(self):
        tipo = ""
        while tipo != "y" and tipo != "n":
            tipo = input("Es viajero frecuente? (y/n): ")
            if tipo == "y":
                self.__agregar_pasajero(True)
            else:
                self.__agregar_pasajero(False)

    # Private methods
    def __agregar_pasajero(self, es_frecuente):
        if es_frecuente:
            pasajero = Frecuente()
        else:
            pasajero = Pasajero()
        pasajero.captura()
        self.pasajeros.append(pasajero)

    # Setters and Getters
    @property
    def pasajeros(self):
        return self.__pasajeros

    @pasajeros.setter
    def pasajeros(self, pasajeros):
        self.__pasajeros = pasajeros