#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #1 Script language

cadena = "Hola mundo! (Por paso de parametro)"

listaReservada = "\nEstas son las palabras reservadas por Python,"
listaReservada += " algunas de ellas las veremos durante el curso:"
listaReservada += "\nand \nexec \nnot \nassert \nfinally \nor \nbreak \nfor"
listaReservada += "\npass \nclass \nfrom \nprint \ncontinue \nglobal \nraise"
listaReservada += "\ndef \nif \nreturn \ndel \nimport \ntry \nelif \nin \nwhile"
listaReservada += "\nelse \nis \nwith \nexcept \nlambda \nyield"

# MAIN
if __name__ == "__main__":
    # Python no proporciona llaves para indicar bloques de código
    # para definiciones de clases y funciones o control de flujo.
    # Los bloques de código se denotan por indentación de línea,
    # que se aplica estrictamente.
    #El número de espacios en la sangría es variable, pero todas
    #las declaraciones dentro del bloque deben sangrarse en la misma cantidad.
    print("Hola mundo!!!")
    """Python permite cadenas de texto que no son asignadas a memoria, como esta.
    Dichas cadenas sirven para realizar comentarios largos. """
    print(cadena)
    # El punto y coma (;) permite múltiples instrucciones en una sola línea,
    # dado que ninguna de las instrucciones inicia un nuevo bloque de código.
    print(listaReservada); raw_input("\n\nPresióna enter para continuar.")
