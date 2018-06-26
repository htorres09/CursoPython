#!/usr/bin/python
# -*- coding: utf-8 -*-
# Práctica de Python #11 Archivos JSON

# Uno de los formatos para guardar y mover información en este momento es JSON
# Y Python soprta JSON de manera nativa, por lo que ahondaremos un poco en el tema
# Para iniciar, importamos la libreria <json>
import json

# El proceso de codificar JSON se llama serialización. El proceso de decodificación
# se llama deserialización
""" >>> Methods: json
    json.dump(<data>,<file_json>)
        - Serializa <data> para escribir en un archivo JSON <file_json>
    json.dumps(<data>[, indent=<N>])
        - Serializa <data> para escribir en una cadena de Python. Si se usa el
          parametro indent=<N> realiza la identación con un numero <N> de espacios
    json.load(<file_json>)
        - Deserializa un archivo JSON <file_json> para escribirla en un objeto
    json.loads(<json_string>)
        - Deserializa los datos consumida de otro programa u obtenida de una cadena
          en formato JSON in Python <json_string>
"""

# JSON importa los datos al archivo de manera diferente a los archivos comunes
data = {
    "presidente":{
        "nombre": "Zaphod Beeblebrox",
        "especie": "Betelgeusian"
    }
}

# Para salvar la información de data a un disco debemos escribirla en el archivo
# usando el manejador de contexto de Python, creando un archivo llamado ej111.json
# abriendolo y escribiendo en el
with open("ej111.json", "w") as escritura:
    json.dump(data, escritura)

# para escribirlo en una cadena String en Python
json_string1 = json.dumps(data, indent = 4)
print("Los datos bajo enconde JSON: ", json_string1)

# Para deserializar la información de un archivo a disco, usamos nuevamente el
# manejador de contexto de python
with open("ej112.json", "r") as lectura:
    data = json.load(lectura)

print("Los datos bajo enconde JSON: ", data)

json_string2 = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string2)
print("Los datos bajo enconde JSON: ", data)

# MAIN
if __name__ == "__main__":
    """ Como ejercicio, se cargara el archivo ej112.json en una variable llamada
    listaTareas
    Utlizar un ciclo para que por cada tarea en listaTarea se debe agregar a un
    arreglo de listas por usuario (listarTareasUsuario["userId"])
    Utilizar la funcion para organizarlas:
        top_usuarios = sorted( listarTareasUsuario.items(),
            key = lambda x: x[1], reverse= True )
    """
