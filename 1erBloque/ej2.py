#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #2 Variables

# Las variables en Python no necesitan de una declaración explicita para
# reservar espacio en memoria. Esta ocurre automáticamente cuando se le asigna
# un valor a una variable.
# El signo (=) es usado para asignar los valores a una variable."""

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
a = 1
b = 2

""" >>> Palabra reservada: del
También puede eliminar la referencia a un objeto numérico utilizando la
instrucción del. La sintaxis la palabra reservada del es:
    del var1 [, var2 [, var3 [...., varN]]]]
Puede eliminar un único objeto o varios objetos utilizando la instrucción del"""

# MAIN
if __name__ == "__main__":
"""Como Ejercicio imprime los valores entero, flotante, y cadena"""
