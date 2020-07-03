#!/usr/bin/expect
set timeout -1

spawn python App.py

# Factura al Contado
expect "Ingrese la opcion deseada: "
send -- "1\r"
expect "Ingrese el porcentaje de descuento: "
send -- "5\r"
expect "Ingrese el nombre del cliente: "
send -- "Juan Perez\r"
expect "Ingrese la direccion del cliente: "
send -- "Residencias Los Arcos, Casa 5\r"
expect "Ingrese el porcentaje de impuesto: "
send -- "12\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "001\r"
expect "Description: "
send -- "Filtro de Aceite AB001\r"
expect "Valor: "
send -- "25000\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "002\r"
expect "Description: "
send -- "Aceite Valvoline semisintético GX700\r"
expect "Valor: "
send -- "18000\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "003\r"
expect "Description: "
send -- "Mano de obra\r"
expect "Valor: "
send -- "10000\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "n\r"

# Factura a Credito
expect "Ingrese la opcion deseada: "
send -- "2\r"
expect "Ingrese el plazo de credito en meses: "
send -- "12\r"
expect "Ingrese el nombre del cliente: "
send -- "Juan Perez\r"
expect "Ingrese la direccion del cliente: "
send -- "Residencias Los Arcos, Casa 5\r"
expect "Ingrese el porcentaje de impuesto: "
send -- "12\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "C001\r"
expect "Description: "
send -- "Rack Thuel #2020-600\r"
expect "Valor: "
send -- "320000\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "C002\r"
expect "Description: "
send -- "2 Llantas R22x12x125 Pirelli\r"
expect "Valor: "
send -- "112000\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "C003\r"
expect "Description: "
send -- "Estribos para Rav4 2017 Plateados\r"
expect "Valor: "
send -- "86000\r"


expect "Desea agregar un detalle de compra? (y/n): "
send -- "y\r"
expect "Codigo: "
send -- "C004\r"
expect "Description: "
send -- "Mano de obra\r"
expect "Valor: "
send -- "25000\r"

expect "Desea agregar un detalle de compra? (y/n): "
send -- "n\r"

# Imprimir los resultados
expect "Ingrese la opcion deseada: "
send -- "3\r"
expect ""
send -- "\r"

# Salir del programa
expect "Ingrese la opcion deseada: "
send -- "4\r"