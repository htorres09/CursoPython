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
# usa las keyword para asignar los valores
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

imprimirParametros(5, 10, 25, 30, 45, 50)

# * Funciones anonimas
# Llamadas así por que no son declaradas de la manera estandar usando <def>. Se
# puede usar la palabra reservada <lambda>. 
# ** Las formas lambda pueden tomar cualquier numero de argumentos pero solo regresan
#    un solo valor en forma de expresión. No puden contener comandos ni multiples
#    expresiones
# ** Una función anonima no puede ser una llamada directa a <print> debido a que
#    lambda requiere una expresión
# ** Las funciones lambda tienen su propio namepspace y no pueden acceder a otras
#    variables que no esten en su lista de parametros o aquellas definidas globalmente
# ** Aunque parece que las funciones lambdas son una versión de una línea de una
#    una función, no son el equivalente de las inline statements en C o C++

""" >>> Palabra reservada: lambda
La syntaxis de <lambda> contienen una sola sentencia de la siguiente manera:
    lambda [arg1 [, arg2, ... , argN]]:<expresion>
"""

# El siguiente es un ejemplo de como utilizar <lambda>
# La definición de la forma <lambda>
suma = lambda arg1, arg2: arg1 + arg2

# llamada a la suma como función
print("Valor total : ", suma(10,29))
print("Valor total : ", suma(15,15))

# MAIN
if __name__ == "__main__":
    """ Como ejercicio crea una función fuera del #MAIN en la que puedas cargar
    diferentes parametros, para llenar una lista de nombres.
    Crea una segunda función pasando como parametro la lista de nombres, y despliega
    un mensjaje mosntrando el nombre de la persona y preguntando su edad
    Crea una función que tome como argumentos la lista de nombres y la lista de edades
    y dentro de ella usa una función anomima para concatenar el nombre de la persona
    y su edad.
    """
