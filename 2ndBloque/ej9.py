#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #9 Funciones

# Una función es un bloque organizado, rehusable que realiza una acción. Las
# funciones proveen de una mejor modularidad para la aplicación y un alto grado
# de reutilizamiento de código

# Definir una función
# Se pueden definir funciones para proveer de ciertas funcionalidades requeridas
# Los bloques de función comienzan con la keyword <def> seguida de parentesis ()
# Los parametros de entrada o argumentos deben ser colocados entre estos parentesis
# La primer sentencia (opcionalmente) puede ser una linea de documentación de la
# función o 'docstring'
# El bloque de código inicia después de dos puntos (:) y llevan identación
# La expresión de retrono, termina y sale de la función, opcionalmente regresando
# dicha expresión al 'caller'. Una sentencia de retrono sin argumentos es lo mismo
# a un return none

""" >>> Palabra Reservada: def
Es la sentencia que se utiliza para definir una función definida por el usuario
def <nombreFuncion> (<parametros>):
    'docstring'
    enunciado(s)
    return [<expresion>]
"""

# Un ejemplo sencillo de una función
def imprimirNVeces(num):
    """
    Función para imprimir una serie de numeros consecutivos
    parametros:     <num> : Numero entero
    salida:         Impresión en pantalla de la cadena y los numeros en el rango
    """
    for n in range(num):
        print("Numero: ", n)
    return
# La identación es muy importante pare definir que parte del bloque es parte de
# la funución
# Para llamar a la función solo usamos el 'caller'
imprimirNVeces(5)

# Todos los argumentos de funciones en Python son pasados por referencia. Es decir
# que si cambias el valor de un argumento en una función, el cambio se refleja también
# fuera de ella
def cambiarParam(lista):
    """ Función para cambiar valores en los argumentos """
    print("Valores dentro de la lista antes del cambio: ", lista)
    lista[-1] = 50
    print("Valores dentro de la lista después del cambio: ", lista)
    return

miLista = [10, 2, 30, 4, 5]
cambiarParam(miLista)
print("Valores fuera de la función: ", miLista)

# Las funciones pueden usar los siguientes tipos de argumentos
#   * Requeridos
# Son parametros no opcionales. Los cuales deben estar en el orden correcto
def imprimirParametroNVeces(cadena, num):
    for n in range(num):
        print(cadena)
    return

imprimirParametroNVeces("hola", 4)

#   * Keyworded
# Son parametros que pueden ser colocados en cualquier orden, ya que el interprete
# usa las keyword para asignar los Valores
imprimirParametroNVeces(num= 4, cadena="hola")

#   * Default
# Son parametros que tienen un valor default si no se le provee uno
def imprimirParametroNVeces(cadena="Hola de nuevo", num):
    for n in range(num):
        print(cadena)
    return

imprimirParametroNVeces(num= 4)

#   * De largo variable
# En ocasiones necesitamos que una función procese más argumentos de los especificados
# estos argumentos son no son nombrados en la definición de la función
def imprimirParametros(cadena, *varTuple):
    print("La salida es: ")
    print(cadena)
    for var in varTuple:
        print(var)
    return

imprimirParametros(5, 10, 25, 30, 45, 50 )
