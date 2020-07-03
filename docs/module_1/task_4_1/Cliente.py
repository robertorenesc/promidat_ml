from Base import Base

class Cliente(Base):
    
    # Constructor
    def __init__(self):
        self.__nombre = ""
        self.__direccion = ""
    
    # Public methods
    def __str__(self):
        return " * Cliente:\n" \
               "\t- Nombre:    %s\n" \
               "\t- Direccion: %s\n" % (self.nombre, self.direccion)

    def captura(self):
        self.nombre = input("Ingrese el nombre del cliente: ")
        self.direccion = input("Ingrese la direccion del cliente: ")

    # Getters and Setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
