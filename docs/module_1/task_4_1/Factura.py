from Base import Base
from Cliente import  Cliente
from Compra import Compra

class Factura(Base):
    
    # Constructor
    def __init__(self):
        self.__porcentaje_impuesto = 0.0
        self.__cliente = Cliente()
        self.__compras = []

    # Public methods
    def monto_subtotal(self):
        total = 0.0
        for i in range(len(self.compras)):
            total += (self.compras[i].monto_compra)
        return total

    def __total_impuesto(self):
        subtotal = self.monto_subtotal()
        return subtotal * self.porcentaje_impuesto / 100

    def monto_total(self):
        return self.monto_subtotal() + self.__total_impuesto()

    def __str__(self):
        text = " DETALLE DE LA FACTURA\n%s\n%s%s" \
               % (self.DOUBLE_LINE_SEPARATOR, str(self.cliente), self.LINE_SEPARATOR)

        for i in range(len(self.compras)):
            text += str(self.compras[i])
               
        text += "%s * Monto Total:         %.2f\n" \
               " * Impuesto:            %.2f%%\n" \
               " * Total + Impuesto:    %.2f\n" \
               % (self.LINE_SEPARATOR, self.monto_subtotal(), self.porcentaje_impuesto, self.monto_total())
        
        return text
    
    def captura(self):
        self.cliente.captura()
        self.porcentaje_impuesto = int(input("Ingrese el porcentaje de impuesto: "))
        option = "y"
        while option != "n":
            option = input("\nDesea agregar un detalle de compra? (y/n): ")
            if option == "y":
                compra = Compra()
                compra.captura()
                self.compras.append(compra)
                print("Compra agregada a la factura.")

    # Getters and Setters
    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto

    @porcentaje_impuesto.setter
    def porcentaje_impuesto(self, porcentaje_impuesto):
        self.__porcentaje_impuesto = porcentaje_impuesto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def compras(self):
        return self.__compras

    @compras.setter
    def compras(self, compras):
        self.__compras = compras
