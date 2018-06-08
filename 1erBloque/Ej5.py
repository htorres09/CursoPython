#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #4 Herramientas de Control - while

# Al contrario del ciclo <for> que se repite un numero finito de veces
# en ocasiones no conocemos el numero de iteraciones que nos tomara
# una serie de sentencias pero tenemos una condición de paro. Para
# dichas operaciones tenemos el ciclo <While>

""" >>> Palabra reservada: while
Un ciclo <while> ejecuta los enunciados mientras una cierta condicion
sea cierta. La sintaxis de la palabra reservada <while> es:
    while <expresion>:
        enunciado(s)
Recuerda que es necesario identar el código, todo lo que este en el mismo
nivel se ejecutara dentro del bloque de nuestra sentencia <while>.
"""

# Un ejemplo sencillo de una cuenta hasta un numero N
n = int(raw_input("Hasta que numero desea contar: "))
count = 0
while (count < n):
    print("La cuenta es:", count )
    count += 1

# Se debe tener precaución pues un ciclo se puede volver infinito sin
# la condicion correcta
v = 1
while v == 1:
    num = int(raw_input("Si quiere detener el ciclo escriba 1: "))
    if (num = 1):
        v += 1
    else:
        print("Cierre el ciclo por favor")
# Los ciclos infinitos pueden ser útiles cuando se usa en esquema de
# cliente-servidor donde el servidor debe correr continuamente para
# que el cliente pueda comunicarse con el servidor.

# MAIN
if __name__ == "__main__":
    """ Como ejercicio
    """
