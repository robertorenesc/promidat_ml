from Base import Base

class Pasajero(Base):

    def __init__(self):
        self.__precio_tiquete = 0.0
        self.__codigo = ""
        self.__nombre = ""
        self.__porcentaje_impuesto = 0.0

    # Public methods
    def total_pagar(self):
        return self.precio_tiquete + self.precio_tiquete * self.porcentaje_impuesto / 100

    def captura(self):
        self.precio_tiquete = float(input("Precio del tiquete: "))
        self.codigo = input("Codigo: ")
        self.nombre = input("Nombre: ")
        self.porcentaje_impuesto = float(input("% Impuesto: "))

    def __str__(self):
        return " * Pasajero: \n" \
               " \t- Precio:        %.2f\n" \
               " \t- Codigo:        %s\n" \
               " \t- Nombre:        %s\n" \
               " \t- Impuesto:      %.2f\n" \
               " \t- Total a Pagar: %.2f\n" \
               % (self.precio_tiquete, self.codigo, self.nombre, self.porcentaje_impuesto, self.total_pagar())

    # Setters and Getters
    @property
    def precio_tiquete(self):
        return self.__precio_tiquete

    @precio_tiquete.setter
    def precio_tiquete(self, precio_tiquete):
        self.__precio_tiquete = precio_tiquete

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo 

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def porcentaje_impuesto(self):
        return self.__porcentaje_impuesto

    @porcentaje_impuesto.setter
    def porcentaje_impuesto(self, porcentaje_impuesto):
        self.__porcentaje_impuesto = porcentaje_impuesto
