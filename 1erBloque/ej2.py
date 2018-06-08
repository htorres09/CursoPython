#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #2 Variables - Números

# Las variables en Python no necesitan de una declaración explicita para
# reservar espacio en memoria. Esta ocurre automáticamente cuando se le asigna
# un valor a una variable.
# El signo (=) es usado para asignar los valores a una variable.

entero = 100                 # Asignación de un número entero (integer)
flotante = 10.9              # Asignación de un número de punto flotante (float)
cadena = "Escribe tu nombre" # Asignación de cadena de texto (string)

# Python permite la asignación de un valor a múltiples variables.
a = b = c = 10

# O puedes asignar múltiples objetos a múltiples Variables
a,b,c = 1,2,"Hola mundo!"

# Python tiene cinco tipos de datos estandar
standarData = "Number, String, List, Tuple, Dictionary"

"""Numbers - Guardan valores númericos"""
a = 99
b = 0.9

""" >>> Palabra reservada: del
También puede eliminar la referencia a un objeto numérico utilizando la
instrucción del. La sintaxis de la palabra reservada <del> es:
    del var1 [, var2 [, var3 [...., varN]]]]
Puede eliminar un único objeto o varios objetos utilizando la instrucción <del>
"""

# Ahora vamos a ver como podemos ingresar datos a nuestro programa.

""" >>> Built-in Function: raw_input()
Para ingresar valores a una variable se usa mediante la asignación con esta
función. La sintaxis de la función <raw_input> es:
    var1 = raw_input("<mensaje>")
La función guarda nuestro valor en formato string
"""

# Para este ejemplo usaremos un nombre y la edad
name = raw_input("Cual es tu nombre: ")
age = int(raw_input("Cual es tu edad: "))
print("Te llamas " + name + " y tienes " + str(age) + " años." )

# Pueden ver que se usaron otras dos funciones <int()> y <str()> esto se debe a
# que raw_input guarda los valores en formato de cadena de texto, y para asignarlos
# a otro tipo usamos los siguientes 'casters'
#       bin() -> binario
#       bool() -> boleano
#       chr() -> un solo caracter
#       float() -> flotante
#       hex() -> hexadecimal
#       int() -> entero
#       long() -> numero largo
#       oct() -> octeadecimal
#       str() -> String
#       unicode() -> unicode
# Utilizamos el 'caster' <str()> para poder concatenar una cadena de caracteres y
# así imprimir nuestro mensaje de resultado

# MAIN
if __name__ == "__main__":
    """ Como Ejercicio imprime los valores entero, flotante, y cadena.
    Después elimina el valor de a, b c con la función del y asigna nuevos valores.
    Imprime los nuevos valores y la suma con el siguiente formato:
        > a + b + c = {val1} + {val2} + {val3} = {total}
    Para terminar, pide que el usuario oprima una tecla para salir.
    Tip: Recuerda, la indentación en Python es importante."""
