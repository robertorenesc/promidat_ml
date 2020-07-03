from Factura import Factura

class FacturaContado(Factura):
    
    # Constructor
    def __init__(self):
        Factura.__init__(self)
        self.__porcentaje_descuento = 0.0

    # Public methods
    def total_con_descueto(self):
        return self.monto_total() - (self.monto_total() * self.porcentaje_descuento / 100)

    def __str__(self):
        return "%s * %% Descuento:          %.2f%% \n" \
               " * Total con Descuento: %.2f\n%s" \
               % (super().__str__(), self.porcentaje_descuento, self.total_con_descueto(), self.DOUBLE_LINE_SEPARATOR)

    def captura(self):
        print("Ingreso de datos de Factura al Contado")
        print("--------------------------------------\n")
        self.__porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
        super().captura()

    # Getters and Setters
    @property
    def porcentaje_descuento(self):
        return self.__porcentaje_descuento

    @porcentaje_descuento.setter
    def porcentaje_descuento(self, porcentaje_descuento):
        self.__porcentaje_descuento = porcentaje_descuento
