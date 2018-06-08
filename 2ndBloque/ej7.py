#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #7 Estructuras de Datos - Tuplas

# La Tupla es una secuencia inmutable de objetos.
# A diferencia de las listas, las tuplas no pueden ser cambiadas como las Listas
# Para declarar una tupla se pueden poner valores entre parentesis y separados por
# comas, o simplemente escribir la secuencia separadas por comas

tupla1 = [1, 2, 3, 4, 5]
tupla2 = "a", "b", "c", "d", "e"
tupla3 = ('física', 'matemática', 1996, 2018)

# Una tupla vacía se puede creear escribiendo dos parentesis vacíos
tupla4 = ();
# Para una tupla de un unico valor se debe escribir la coma al final
tupla5 = (10,);

# Podemos acceder a los valores de una lista por medio de su indice
print("Tupla 1[0]", tupla1[0])
# O podemos acceder a varios valores usando un rango de indices
print("Tupla 2[2:4]", tupla2[2:4])
# Esto también es cierto para acceder desde el inicio a una posición determinada
# O desde una posición determinada hasta el final
print(tupla1[:2])
print(tupla1[2:])
# O acceder desde el ultimo elemento hacia atras usando indices negativos
print("Año: ", tupla3[-1])
print("Materia: ", tupla[-4])

# Debido a que son inmutables no se pueden actualizar o cambiar sus valores
# por lo que la siguiente es una acción invalida
tupla3[2] = "2000"
# Pero podemos crear una nueva tupla usando los valores de otras
tupla6 = tupla1[:2] + tup3 + tup[2:]
print(tupla6)
# Para borrar una tupla podemos usar la palabra reservada <del>
del tupla3
if (tupla3):
    print("Existe ", tupla3)
else:
    print("No existe")

# Entre las operaciones básicas de las tuplas se puede conocer su longitud
print(len(tupla6))

# Se pueden concatenar
tupla3 = (1,2,3) + (4,5,6)
print(tupla3)

# Se puede crear tuplas de repetición
tupla = ("Hola",) * 4
print(tupla)

# Se puede conocer si un elemento existe en la lista
print("matemáticas" in tupla3)

# Y como vimos en el tema de ciclos, se puede iterar sobre ellas
for x in tupla: print(x, end=' ')

# Las funciones <max> y <min> se pueden aplicar también con Tuplas
print(max(tupla2))
print(min(tupla3))

#O podemos convertir una lista en una tupla
lista = ["Manaza", "Peras", "Naranjas", "Sandia", "Uvas"]
nuevaTupla = tuple(lista)

# MAIN
if __name__ == "__main__":
    """ Como ejercicio pide al usuario dos numeros <n> y <m>
    Usando la siguente sentencia crea las tuplas <t1> y <t2>:
        t1 = (random.randint(0,99),) * n
        t2 = (random.randint(0,99),) * m
    Crea un ciclo que compare si cada elemento de <t1> existe en la <t2>
    Si existe, almacenarlo en una nueva tupla <t3>
    Imprimir las longitudes de las tres tuplas, sus máximos y sus minimos.
    """
