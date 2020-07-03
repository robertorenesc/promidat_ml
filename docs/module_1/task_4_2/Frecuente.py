from Pasajero import Pasajero

class Frecuente(Pasajero):

    # Constructor
    def __init__(self):
        super().__init__()
        self.__descuento = 0.2

    # Public methods
    def total_pagar(self):
        total = super().total_pagar()
        return total - total * self.descuento

    def __str__(self):
        return "%s" \
               " \t- Pasajero Frecuente (Descuento: %.2f)\n" % (str(super().__str__()), self.descuento)       

    # Setters and Getters
    @property
    def descuento(self):
        return self.__descuento

    @descuento.setter
    def descuento(self, descuento):
        self.__descuento = descuento