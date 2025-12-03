

"""

Un string es de manera sencilla una serie de caracteres

En python todo lo que se  ENCUENTRE DENTRO DE COMILLAS SIMPLES 
' ' O DOBLES COMILLAS " "
es considerado un STRING
por ejemplo:

  "Esto es un string"
  'Esto tambien es un string'

  'Le dije a mi amigo, "Python es mi lenguaje favorito"'
   " El lenguaje 'PYTHON' lleva el nombre en honor a Monty Python, no por la serpiente "
"""

# STRINGS 

name = "clase de programacion" 
print(name)
print()
print(name.title())
print (name)
print()

"""
un metodo es una accion que python 
puede realizar en un fragmento de datos o
sobre una variable.
El punto (.) despues de una variable string
seguido del metodo title() dice que se tiene que ejecutar el metodo
title() de la variable name.

Todos los metodos van seguidos de parentesis 
porque en ocasiones necesitan informacion adicional para funcionar, lo cual iria dentro 
de los parentesis.

En esta ocasion el metodo .title() no requiere informacion adicional para ejecutarse.

"""


# OTROS METODOS
print("Para mayusculas: ", name.upper())
print("Para mayusculas: ", name.lower())



# CONCATENACION DE STRINGS

first_name = "Charly"
last_name = "Mercury"
full_name = first_name + " " + last_name
print(full_name)
print("Hola", "¡" + full_name.title() + "!")

message = print("Hola", "¡" + full_name.title() + "!")
print(message)


# Whitespaces
"""
Whitespace se refuere a cualquier caracter que no se imprime, es decir, un espacio en blanco, un tabulador o
un salto de linea.
Los whitespaces se utilizan comunmente para organizar las salidas en pantalla de tal manera que sea mas amigable 
de leer o ver para los usuarios.
"""

print("Python")
print("\tPython") # Tabulador antes de Python
print("\t\tPython") # Tabulador antes de Python
print("Languajes: \n Python\n C\n JavaScript") # Salto de linea

# Eliminando Whitespaces



favorite_language = "Python"
print(favorite_language)
print(favorite_language.rstrip()) #Elimina espacios en blanco a la derecha
print(favorite_language.lstrip()) # Elimina espacios en blanco a izquierda
print(favorite_language.strip()) # Elimina espacios en blanco a ambos lados

# Syntax Error con Strings
message = 'Una fortaleza de Python es su comunidad activa.'
print(message) 
message_ = 'Una fortaleza de "Python" es su comunidad activa.'


# F - STRINGS PARA CONCATENACION

first_namee = "charly "

last_namee = "mercury"

full_name = f"{first_namee.title()} {last_name}"


"""

Ejercicio:
Imprime el nmombre de un personaje famoso y una cita famosa que haya dicho

Ejemplo:

CHARLY MERCURY UNA VEZ DIJO EL 103 ES MI GRUPO FAVORITO

"""

personaje_famoso = "leo"

apellido_personaje_famoso = "messi"

cita = '"Me preocupa mas ser buena personaje que ser el mejor del mundo"'

full_namee = f"{personaje_famoso.title()} {apellido_personaje_famoso} una vez dijo {cita}"

print(full_namee)

