#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #10 Archivos

# Hasta el momento solo hemos usado las entradas y salidas estandar.
# Python provee de funciones básicas y métodos para manipular archivos, todo usando
# el objeto <file>.

# Antes de leer o escribir un archivo, se debe usar la función <open>
""" >>> Built-in Function: open()
Esta funición abre un archivo y regresa un objeto <file>. Si el archivo no puede
ser abierto, regresa un mensaje de error.
La sintaxis de la función <open> es:
    open(<archivo> [, <modo_de_acceso>][, <buffering>])
    <archivo>:
      Es un string que contiene el nombre del archivo o la ruta donde se encuentra
    <modo_de_acceso>:
        Determina en que modo se abre el archivo, ya sea lectura, escritura, etc.
        Ver lista de modos de acceso
    <buffering>:
        Si el valor es 0, no se realiza ningún buffering. Si es uno, un buffering
        de linea es realizado accesando al archivo; si el valor del entero es mayor
        a uno, se abre una línea de buffering del tamaño especificado
"""

""" >>> Modos de acceso
Caracter    Significado
    'r'     abrir para lectura (default)
    'w'     abrir para escritura, truncando primero el archivo
    'x'     abrir para crear exclusivamente, falla si el archivo existe
    'a'     abrir para escritura, agregando al final del archivo si existe
    'b'     modo binario
    't'     modo texto (default)
    '+'     abrir el archivo en disco para actualizar (lectura y escritura)
"""

""" >>> Atribuitos del objeto file
    file.closed     Regresa true si el archivo esta cerrado
    file.mode       Regresa el modo de acceso con el que fue abierto el archivo
    file.name       Regresa el nombre del archivo
"""

""" >>> Methods: file
    file.close()    - Vacía cualquier información que no este escrita y cierra el
                      archivo
    file.write(<string>)
                    - Escribe una cadena string en un archivo abierto
    file.read([<cuenta>])
                    - Lee una cadena del archivo abierto. Si se usa el parametro
                      lee esa cantidad de bytes, si no, trata de leer lo más
                      posible
    file.tell()     - Regresa la posición actual dentro del archivo
    file.seek(offset[, from])
                    - Cambia la posición actual en el archivo. El argumento <offset>
                      indica el numero de bytes por mover. El argumento <from>
                      indica la posición desde donde son movidos los bytes
"""
# Vamos a abrir un archivo en el mismo nivel de la carpeta en modo lecutra
archivo1 = open("ej101.txt", "r")
print("Nombre del archivo: ", archivo1.name )
print("Esta cerrado o no: ", archivo1.closed )
print("Modo de apertura: ", archivo1.mode )

# Vamos a cerrar el archivo
archivo1.close()
print("Esta cerrado o no: ", archivo1.closed )

# Vamos a escribir en un archivo
archivo2 = open("ej102.txt", "w")
archivo2.write("Hola mundo! \nEstoy escribiendo en un archivo\n")

# Vamos a leer e imprimir en pantalla
cadena = archivo2.read()
print("El archivo contiene: ", cadena )

# Vamos a actualizar nuestro archivo
archivo2 = open("ej101.txt", "w+")
archivo2.write("Hola mundo! \nEstoy escribiendo en un archivo\n")
cadena = archivo2.read()
print("El archivo contiene: ", cadena )

# MAIN
if __name__ == "__main__":
    """ Como Ejercicio genera un archivo que guarde un diccionario de nombres y
    correos
    Que se presente en el siguiente formato
        Nombre                          -   Correo
        "José María Morelos y Pavón"    -   jm.morelos@correo.mx
    """
