#!/usr/bin/expect
set timeout -1

spawn python App.py

# Vuelo comercial
expect "Ingrese la opcion deseada: "
send -- "1\r"

# Vuelo comercial - nacional
expect "Ingrese la opcion deseada: "
send -- "1\r"

# Datos del vuelo Nacional
expect "Numero: "
send -- "1\r"
expect "Hora de Salida: "
send -- "12\r"
expect "Hora de Llegada: "
send -- "13\r"
expect "Minimo de pasajeros: "
send -- "3\r"

#Datos de Pasajero 1
expect "Es viajero frecuente? (y/n): "
send -- "y\r"
expect "Precio del tiquete: "
send -- "320\r"
expect "Codigo: "
send -- "FR001\r"
expect "Nombre: "
send -- "Albert Einstein\r"
expect "% Impuesto: "
send -- "14\r"

#Datos de Pasajero 2
expect "Es viajero frecuente? (y/n): "
send -- "n\r"
expect "Precio del tiquete: "
send -- "320\r"
expect "Codigo: "
send -- "PA001\r"
expect "Nombre: "
send -- "Nicola Tesla\r"
expect "% Impuesto: "
send -- "14\r"

#Datos de Pasajero 3
expect "Es viajero frecuente? (y/n): "
send -- "n\r"
expect "Precio del tiquete: "
send -- "320\r"
expect "Codigo: "
send -- "PA002\r"
expect "Nombre: "
send -- "Isaac Newton\r"
expect "% Impuesto: "
send -- "14\r"
expect "Desea agregar un nuevo pasajero al vuelo? (y/n): "
send -- "n\r"

expect "Ingrese la opcion deseada: "
send -- "2\r"

# Datos del vuelo Internacional
expect "Numero: "
send -- "2\r"
expect "Hora de Salida: "
send -- "18\r"
expect "Hora de Llegada: "
send -- "23\r"
expect "Pais: "
send -- "Holanda\r"

# Datos de pasajero Internacional 1
expect "Desea agregar un nuevo pasajero al vuelo? (y/n): "
send -- "y\r"
expect "Es viajero frecuente? (y/n): "
send -- "n\r"
expect "Precio del tiquete: "
send -- "640\r"
expect "Codigo: "
send -- "PA003\r"
expect "Nombre: "
send -- "Ayrton Senna\r"
expect "% Impuesto: "
send -- "16\r"

# Datos de pasajero Internacional 2
expect "Desea agregar un nuevo pasajero al vuelo? (y/n): "
send -- "y\r"
expect "Es viajero frecuente? (y/n): "
send -- "y\r"
expect "Precio del tiquete: "
send -- "640\r"
expect "Codigo: "
send -- "FR002\r"
expect "Nombre: "
send -- "Nicky Lauda\r"
expect "% Impuesto: "
send -- "16\r"

expect "Desea agregar un nuevo pasajero al vuelo? (y/n): "
send -- "n\r"

expect "Ingrese la opcion deseada: "
send -- "3\r"

expect "Ingrese la opcion deseada: "
send -- "2\r"

# Datos del vuelo de Carga
expect "Numero: "
send -- "3\r"
expect "Hora de Salida: "
send -- "18\r"
expect "Hora de Llegada: "
send -- "23\r"
expect "Peso maximo: "
send -- "3500\r"

expect "Ingrese la opcion deseada: "
send -- "3\r"

expect "> Fin de la Lista"
send -- "\r"

expect "Ingrese la opcion deseada: "
send -- "4\r"