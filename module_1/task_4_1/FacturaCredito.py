from Factura import Factura

class FacturaCredito(Factura):
    
    # Constructor
    def __init__(self):
        Factura.__init__(self)
        self.__plazo_credito = 3

    # Public methods
    def __calcular_cuotas(self):
        return self.monto_total() / self.plazo_credito
    
    def __str__(self):
        return "%s * Meses plazo:         %i \n" \
               " * Cuota mensual:       %.2f \n%s" \
               % (super().__str__(), self.plazo_credito, self.__calcular_cuotas(), self.DOUBLE_LINE_SEPARATOR)

    def captura(self):
        print("Ingreso de datos de Factura a Credito")
        print("--------------------------------------\n")
        self.plazo_credito = int(input("Ingrese el plazo de credito en meses: "))
        super().captura()

    # Getters and Setters
    @property
    def plazo_credito(self):
        return self.__plazo_credito

    @plazo_credito.setter
    def plazo_credito(self, plazo_credito):
        self.__plazo_credito = plazo_credito
