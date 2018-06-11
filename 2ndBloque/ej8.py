#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #8 Estructuras de Datos - diccionarios

# Los diccionarios son elementos muy útiles que pueden ser escritos como parejas
# de llave-valor separados por ':', y estos elementos separados por comas. Todo
# escrito entre corchetes '{}'.
# Las llaves deben ser unicas en los diccionarios, mientras que los valores no
# necesariamente. Los valores dentro de un diccionario pueden ser de cualquier tipo
# pero las llaves devben ser de un tipo de dato inmutable como Strings, numeros o tuplas.

dict = {'Nombre': 'Zara', 'Edad': 19, 'Clase': 'Física' }

# Podemos acceder a los valores por medio de su llave
print("dict['Nombre']: ", dict['Nombre'])

# Para actualizar los valores de un dicionario basta con asignar el valor a la llave
dict['Edad'] = 20
print("dict['Edad']: ", dict['Edad'])

# Para eliminar un elemento individual usamos <del> y la llave que queremos remover
del dict['Clase']
# Si queremos eliminar todo el diccionario
del dict

# Los valores en un diccionario no tienen restricciones, pueden ser de cualquier
# tipo. Pero esto no es cierto para las llaves. Solo una llave por entrada es valida.
# ¿Cuál nombre crees que se imprima en pantalla?
dict = {'Nombre': 'Zara', 'Edad': 19, 'Nombre': 'Sarah' }
print("dict['Nombre']: ", dict['Nombre'])

# Se pueden usar operaciones básicas sobre los diccionarios
# Por ejemplo la longitud del diccionario. Es decir, el numero de sus elementos
dict = {'Nombre': 'Zara', 'Edad': 19, 'Clase': 'Física' }
print(len(dict))

# Un diccionario es un objeto en memoria, para impremirlo en pantalla debemos
# convertir lo en una cadena de texto usando <str>
print(str(dict))

# O se puede reconocer su tipo de dato
""" >>> Built-in Function: type()
Esta funición regresa el tipo de un objeto. La sintaxis de la función <type> es:
    type(<objeto>)
Este regresa el tipo del objeto.
"""

# Los diccionarios también tienen sus propios metodos.
""" >>> Methods: Dictionaries
    dict.clear()          - Remueve todos los elementos de una lista
    dict.copy()           - Crea una copia del diccionario
    dict.fromkeys(<seq>)  - Crea un diccionario usando una secuencia como llaves
    dict.get(<key>)       - Regresa el valor de la Llave <key>
    dict.items()          - Regresa una lista parejas de tuplas del diccionario
                            (llave, valor)
    dict.keys()           - Regresa una lista de llaves del diccionario
                          - Remueve y regresa el ultimo objeto de una lista
    dict.setdefault(<key>, <optional>)
                          - Similar a get, pero da un valor asocioado <optional>
                            a la llave
    dict.update(<dict2>)  - Agrega el contenido del nuevo diccionario <dict2> al
                            diccionario
    dict.values()         - Regresa una lista de valores del diccionario
"""
# Vamos a crear un diccionario a partir de la siguiente secuencia
seq = ('nombre', 'edad', 'sexo')
dict1 = dict1.fromkeys(seq)
print("Diccionario: ", str(dict1))
# Vamos a darles valores a nuesto diccionarios
dict1['nombre'] = 'Ana'
dict1['edad'] = 19
dict1['sexo'] = 'Mujer'
# Vamos a crear dos copias de nuestro diccionario
dict2 = dict.copy()
dict3 = dict.copy()
# Borremos el diccionario 3
dict3.clear()
# Agreguemos contenido al diccionario 3
dict3.setdefault('carrera', 'Computación')
# Y ahora agregamos el contendio del diccionario 3 al 2
dict2.update(dict3)
# Vamos a imprimer una lista de llaves en el diccionario 2, luego una lista de
# valores
print("Llaves: ", dict2.keys())
print("Valores: ", dict2.values())
# Ahora vamos a imprimir el nombre y la edad del diccionario 1
print(dict['nombre'])
print(dict.get('edad'))
# para finalizar imprimiremos una lista de tuplas del diccionarios
for key, value in dict.items()
    print(key + ": " + value)

# MAIN
if __name__ == "__main__":
    """ Como Ejercicio genera una diccionaria a partir de la siguiente secuencia
        nombre, edad, numeroFavorito
    Y llenarlo con su nombre su edad y un numero entre 0 y 11 sin incluirlos (0-10)
    Crea un segundo diccionario con los siguientes elementos
        leche, salchicha, huevos, melones, papaya, tocino
    Y en un ciclo, pide al usuario escoger una cantidad entre 0 y 10 de ese elemento
    por comprar incluyendo los [0-10].
    Combina los dos diccionarios. Por cada elemento diferente de nombre, edad y
    numeroFavorito, en un ciclo imprime la siguiente oración:
        '<nombre> tiene <edad> años.'
    Si la cantidad asociada al elemento es mayor o igual que su numero favorito
    agregar a la oración lo siguiente:
        'Le gusta el/la <elemento>.'
    Si la cantidad asociada al elemento es menor, agregar:
        'No le gusta el/la <elemento>.'
    """
