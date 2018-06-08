#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #1 Script language

cadena = "Hola mundo!"

# MAIN
if __name__ == "__main__":
    # Python no proporciona llaves para indicar bloques de código para definiciones
    # de clases y funciones o control de flujo.
    # Los bloques de código se denotan por indentación de línea, que se aplica
    # estrictamente. El número de espacios en la sangría es variable, pero todas
    # las declaraciones dentro del bloque deben ser espaciadas en la misma cantidad.

    """ >>> Built-in Function: print()
    Para imprimir valores en pantalla utilizamos esta función. La sintaxis es:
        print(<argumento>)
    Esta imprime cadenas de texto o las variables las convierte en flujo de cadenas
    de texto para mostrarlas en pantalla.
    """
    print("Hola mundo!!!")

    """Python permite cadenas de texto que no son asignadas a memoria, como esta.
    Dichas cadenas sirven para realizar comentarios largos. """

    """ >>> Built-in function: input() """
    # input() muestra el mensaje y luego espera a que el usuario tome una acción.
    # El punto y coma (;) permite múltiples instrucciones en una sola línea,
    # dado que ninguna de las instrucciones inicia un nuevo bloque de código.
    print("A imprimir: ", cadena); input("\n\nPresióna enter para continuar.")
