#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #6 Estructuras de Datos - Listas

# Hasta el momento hemos visto las listas, pero no nos hemos adentrado en ellas.
# La secuencia es la estructura de datos más básica de Python. Cada elemento tiene
# asignado un número, una posición o indice. El primer indice es 0, el segundo 1,
# y así continua.
# Las listas son elementos muy versatiles que pueden ser escritos como valores
# separados por comas y entre brackets. Lo más importante es que no todos los
# elementos de la lista tienen que ser del mismo tipo.

lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c", "d", "e"]
lista3 = ['física', 'matemática', 1996, 2018]

# Podemos acceder a los valores de una lista por medio de su indice
print("Lista 1[0]", lista1[0])
# O podemos acceder a varios valores usando un rango de indices
print("Lista 2[2:4]", lista2[2:4])
# O de una el inicio a una posición determinada
print("Lista2[:3]", lista2[:3])
# O desde una posición determinada hasta el final
print("Lista2[3:]", lista2[3:])
# O acceder desde el ultimo elemento hacia atras usando indices negativos
print("Año: ", lista[-1])
print("Materia: ", lista3[-3])
# Las listas se pueden actualizar usando los indicies del valor que se desee cambiar
print("Lista 3[2]", lista3[2])
lista3[2] = "2000"
print("Lista 3[2]", lista3[2])

# La función print se comporta de manera singular con las listas, si se envía la
# lista como parametro, imprime la lista completa como fue declarada
print(list3)
# Para borrar un elemento de la lista podemos usar la palabra reservada <del> si
# conocemos exactamente cual elemento queremos borrar
del lista3[2]
print(list3)

# Entre las operaciones básicas de las listas se puede conocer su longitud
""" >>> Built-in Function: len()
Esta funición regresa la longitud de un objeto (numero de elementos). La sintaxis
de la función <len> es:
    len(<objeto>)
El argumento puede ser una secuencia (string, bytes, tuplas, listas o un rango)
o bien, una colección (diccionarios, sets)
"""
print(len(lista1))

# Se pueden concatenar dos Listas
lista4 = [1,2,3] + [4,5,6]
print(lista4)

# Se puede crear listas de repetición
lista5 = ["Hola"] * 4
print(lista5)

# Se puede conocer si un elemento existe en la lista
""" >>> Palabra reservada: in
Es usada para probar si en una secuencia contiene un valor. Regresa True si el valor
esta presente, False si no. La sintaxis es:
    <elemento> in <secuencia>
"""
print(3 in lista1)

# Y como vimos en el tema de ciclos, se puede iterar sobre ellas
for x in lista2: print(x, end=' ')

# Tambien podemos conocer el elemento de mayor valor de una lista
""" >>> Built-in Function: max()
Esta funición regresa el elemento de mayor valor. La sintaxis de la función <max> es:
    max(<lista>)
"""
max(lista1)

# Tambien podemos conocer el elemento de menor valor de una lista
""" >>> Built-in Function: min()
Esta funición regresa el elemento de mayor valor. La sintaxis de la función <min> es:
    min(<lista>)
"""
min(lista2)

# Las listas también tienen sus propios metodos.
""" >>> Methods: list
    list.append(<obj>)    - Agrega un objeto a una lista
    list.count(<obj>)     - Regresa cuantas veces ocurre el valor objeto en una
                            lista
    list.extend(<seq>)    - Agrega el contenido de una secuencia a una lista
    list.index(<obj>)     - Regresa el indice de la primera ocurrencia del objeto
                            en la lista
    list.insert(<index>, <obj>)
                          - Inserta un objeto en la la lista en la posición del
                            indice offset
    list.pop(<obj> = list[-1])
                          - Remueve y regresa el ultimo objeto de una lista
    list.remove(<obj>)    - Remueve un objeto de la lista
    list.reverse()        - Cambia una lista a su orden reversa
    list.sort([func])     - Ordena los objetos en una lista, usa comparación si
                            si se le asigna una función
"""
# Vamos a crear una lista rápida
listaRapida = [ 1 ] * 9
# Y le agregamos valores
listaRapida.append(10)
# ahora imprimiremos el numero de elementos '1' en nuestra lista
print("Cantidad de elementos 1 : ", listaRapida.count(1))
# vamos a agregar una secuencia en desorden
listaRapida.extend([4, 2, 8, 2, 11])
# Y vamos a insertar el numero '5' en la posción 0
listaRapida.insert(0, 5)
# Y busquemos ahora cual posición tiene el primer 1
print("Indicie del elemento 1: ", listaRapida.index(1))
# vamos a remover el objeto 1 ver que nos imprime
listaRapida.remove(1)
print(listaRapida)
# eliminemos entonces el ultimo elemento
listaRapida.pop()
# y también la primera aparición del elemento 2
listaRapida.pop(listaRapida.index(2))
# vamos a ordenar los elementos de la lista e imprimirla
listaRapida.sort()
print("Lista: ", listaRapida)
# y ahora la imprimimos en orden inverso
print("Lista: ", listaRapida.reverse())

# MAIN
if __name__ == "__main__":
    """ Como Ejercicio genera una lista con un elemento en blanco
    lista = [' ']
    Y en un ciclo, pide al usuario llenar una lista de vivieres por comprar.
    Imprime la lista y sobre ella busca si el usuario lleva los siguientes articulos:
        leche, salchicha, huevos, melones, papaya, tocino
    De ser así, guarda los indices en otra lista, y remueve dichos elementos
    Usando los elementos de esa segunda lista como indices pide al usuario
    ingresar nuevos vivieres
    Para finalizar, imprime la lista ordenada
    """
