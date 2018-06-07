#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #4 Herramientas de Control - For

# Las funciones iterativas son repeticiones de las mismas acciones con diferentes
# grupos de valores o datos.
# La función <for> nos permite iterar sobre elementos en cualquier secuencia o cadena

""" >>> Palabra reservada: for
Si una secuencia contiene una lista de expresiones, es evaluada primero; después
el primer elemento en la secuencia es asignada a la variable iterativa.
Seguido, los enuncuados en el bloque son ejecutados.
Cada elemento en la lista es asignado a la variable iterativa y los enunciados son
ejecutados por cada una de ellas. La sintaxis de la palabra reservada <for> es:
    for <variable> in <secuencia>:
        enunciado(s)
Recuerda que es necesario identar el código, todo lo que este en el mismo nivel
se ejecutara dentro del bloque de nuestra sentencia <for>.
"""

# Ahora vamos a generar una lista de numeros para iterar sobre ellos.

""" >>> Built-in Function: range()
La función <range> es una función de iteración sobre una secuencia de numeros
genera una iteración de progresión aritmética. La sintaxis de la función <range> es:
    range(<n>)
"""

# Vamos a imprimir una lista de valores de 0 hasta N
numero = int(raw_input("Hasta que numero quiere generar: "))
for valor in range(numero):
    print(valor)

# Pero el ciclo <for> puede ser utilizado para iterar sobre cada elemento de una
# lista, y tomar acciones sobre ella
compras = ["Avena","Platano","Leche","Uvas","Galletas"]
for producto in compras:
    if producto != "Galletas":
        print("Este " + producto + " es una comida saludable")
    else:
        print("Las galletas no lo son")
