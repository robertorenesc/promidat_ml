import os
from VueloInternacional import VueloInternacional
from VueloLocal import VueloLocal
from VueloCarga import VueloCarga

class App():

    # Constructor
    def __init__(self):
        self.__vuelos = list()
    
    # Public methods
    def principal(self):
        respuesta = ""
        while respuesta != "4":
            respuesta = self.__menu()
            # os.system('clear')
            if respuesta == "1":
                self.__secundario()
            if respuesta == "2":
                self.vuelos.append(self.__ingresar_vuelo(False, False))
            if respuesta == "3":
                self.imprimir_vuelos()

    # Private methods
    def __menu(self):
        # os.system('clear')
        print("+--------------------------------------------------+")
        print("|                  Menu Principal                  |")
        print("+--------------------------------------------------+")
        print("|                                                  |")
        print("|     1. Ingresar vuelo comercial                  |")
        print("|     2. Ingresar vuelo de carga                   |")
        print("|     3. Imprimir la lista de vuelos (%i)           |" % len(self.vuelos))
        print("|     4. Salir                                     |")
        print("|                                                  |")
        print("+--------------------------------------------------+")
        print()
        return input("Ingrese la opcion deseada: ")

    def __secundario(self):
        respuesta = ""
        while respuesta != "3":
            respuesta = self.__submenu()
            #os.system('clear')
            if respuesta == "1":
                self.vuelos.append(self.__ingresar_vuelo(True, False))
            if respuesta == "2":
                self.vuelos.append(self.__ingresar_vuelo(True, True))
        
    def __submenu(self):
        #os.system('clear')
        print("+--------------------------------------------------+")
        print("|                  Menu de Vuelos                  |")
        print("+--------------------------------------------------+")
        print("|                                                  |")
        print("|     1. Ingresar vuelo nacional                   |")
        print("|     2. Ingresar vuelo internacional              |")
        print("|     3. Salir                                     |")
        print("|                                                  |")
        print("+--------------------------------------------------+")
        print()
        return input("Ingrese la opcion deseada: ")

    def __ingresar_vuelo(self, es_comercial, es_internacional):
        if es_comercial:
            if es_internacional:
                vuelo = VueloInternacional()
            else:
                vuelo = VueloLocal()
        else:
            vuelo = VueloCarga()
        vuelo.captura()
        return vuelo

    def imprimir_vuelos(self):
        print("\n           Lista de Vuelos Ingresados")
        print("=================================================")
        for i in range(len(self.vuelos)):
            print(self.vuelos[i])
        print("> Fin de la Lista")
        input()

    # Setters and Getters
    @property
    def vuelos(self):
        return self.__vuelos

    @vuelos.setter
    def vuelos(self, vuelos):
        self.__vuelos = vuelos

prueba = App()
prueba.principal()


