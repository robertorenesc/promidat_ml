from Base import Base

class Compra(Base):
    
    # Constructor
    def __init__(self):
        self.__codigo = ""
        self.__descripcion = ""
        self.__monto_compra = 0
    
    # Public methods
    def __str__(self):

        return " * Codigo: %s\n" \
               " \t- Descripcion: %s\n" \
               " \t- Monto:       %.2f\n" \
               % (self.codigo, self.descripcion, self.monto_compra)

    def captura(self):
        print("\nDetalle de la compra:")
        print("---------------------------")
        self.codigo = input("Codigo: ")
        self.descripcion = input("Description: ")
        self.monto_compra = float(input("Valor: "))

    # Getters and Setters 
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def monto_compra(self):
        return self.__monto_compra

    @monto_compra.setter
    def monto_compra(self, monto_compra):
        self.__monto_compra = monto_compra
