#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #2 Herramientas de Control - If Elif Else

# Las funciones de toma de decisiones son para anticipar las condiciones que
# ocurren durante la ejecución del programa y las acciones especificas que se
# realizan de acuerdo a esas condiciones.
# El enunciado If se usa para estas condicionales

""" >>> Palabra reservada: if
Esta es nuestra sentencia que contiene la expresión lógica usando los datos a
comparar y toma la desción basada en el resultado. La sintaxis de la palabra
reservada <if> es:
    if <expresion>:
        enunciado
        ...
        enunciados
Recuerda que es necesario identar el código, todo lo que este en el mismo nivel
se ejecutara dentro del bloque de nuestra sentencia <if>.
"""
verdad = "False"
if verdad :
    print("Ha dicho una verdad")

# El resultado anterior siempre imprime nuestro enunciado, debido a que la sentencia
# if, si no se realiza una comparación logica, por defecto verifica que haya un
# valor en la variable, si no es nula, lo toma como cierto.
# Comprueba cambiando el valor -> verdad = "True"; y después -> verdad = ""; Para
# ver que resultados arroja.

""" >>> Palabra reservada: else
Parte de nuestra sentencia <if>, la palabra reservada <else> sirve para agregar
una segunda opción, de no ser cierta la expresión lógica. La sintaxis de la palabra
reservada <else> en conjunto a <if> es:
    if expresion:
        enunciado
    else:
        enunciado
"""
# Usaremos una función aleatoria (<random()>) para generar nuestra condición al
# azar, aunque de momento no vamos a adentrarnos demasiado en dicha función.
# Crearemos una prueba sencila, si el valor de nuestra variable es moneda es menor
# a 0.5, imprimiremos la palabra "Cara"; en caso de ser igual o mayor a 0.5 va a
# imprimir la palabra "Cruz"
moneda = random.random()    # Asignamos un valor flotante entre el rango de [0.0, 1)
if moneda < 0.5:
    print("Cara")
else:
    print("Cruz")

""" >>> Palabra reservada: elif
Parte de nuestra sentencia <if>, la palabra reservada <elif> sirve para agregar
una nuevas condicionales. De no ser cierta la primer expresión lógica, <elif> se
encarga de revisar si cumple con la siguente condicional.
La sintaxis de la palabra
reservada <else> en conjunto a <if> es:
    if <expresion>:
        enunciado
    elif <expresion>:
        enunciado
    ...
    else:
        enunciado
Python no tiene una sentencia <switch> como otros lenguajes de programación. Para
remplazarla, se usan multiples condiconales <elif>.
"""

valor = int(raw_input("Escoge un numero de 1 al 3"))
if valor == 1:
    print("Has escogido la primera opción")
elif valor == 2:
    print("Has escogido la segunda opción")
elif valor == 3:
    print("Has escogido la ultima opción")
else:
    print("No has escogido una opción valida")

# MAIN
if __name__ == "__main__":
    """ Como Ejercicio pide al usuario hacer una serie de elecciones
    Preguntale por su nombre y edad, si es mayor de 18 años.
    Imprime un mensaje diciendo:
        "{nombre} puede votar."
    Preguntale si gusta refresco o jugo.
    Imprime el siguente mensaje:
        "{nombre} prefiere tomar {elección} en lugar de {no_elegido}"
    Por ultimo preguntale cuantos vasos entre [0 y 10] de su elección pediria.
    Si es 0 imprime:
        "Si {nombre} no toma un vaso, aún tendra sed."
    Si es mayor a 0 y menor a 5 imprime:
        "Si {nombre} toma {n} vasos, calmara su sed."
    Si es mayor a 5 o igual a 10 imprime:
        "Si {nombre} toma {n} vasos, va a tener que ir al sanitario después."
    Si no es ninguna de las opciones imprime:
        "Lo siento no le puedo servir {n} cantidad de vasos"
    """
