import os

from FacturaContado import FacturaContado
from FacturaCredito import FacturaCredito

class App:
    def __init__(self):
        self.__facturas = list()
        
    def __menu(self):
        # os.system('clear')
        print("+--------------------------------------------------+")
        print("|                  Menu Principal                  |")
        print("+--------------------------------------------------+")
        print("|                                                  |")
        print("|     1. Ingresar factura de contado               |")
        print("|     2. Ingresar factura a credito                |")
        print("|     3. Imprimir la lista de facturas (%i)         |" % len(self.__facturas))
        print("|     4. Salir                                     |")
        print("|                                                  |")
        print("+--------------------------------------------------+")
        print()
        return input("Ingrese la opcion deseada: ")

    def __ingresar_factura(self, es_factura_credito = False):
        if es_factura_credito:
            factura = FacturaCredito()
        else:
            factura = FacturaContado()
        factura.captura()
        return factura

    def imprimir_facturas(self):
        print("\n             Lista de Facturas")
        print("=================================================")
        for i in range(len(self.__facturas)):
            print(self.__facturas[i])
        input()

    def principal(self):
        respuesta = ""
        while respuesta != "4":
            respuesta = self.__menu()
            # os.system('clear')
            if respuesta == "1":
                self.__facturas.append(self.__ingresar_factura(False))
            if respuesta == "2":
                self.__facturas.append(self.__ingresar_factura(True))
            if respuesta == "3":
                self.__facturas.append(self.imprimir_facturas())

prueba = App()
prueba.principal()


