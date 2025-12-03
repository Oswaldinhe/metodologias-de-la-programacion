# Functions
"""


Las dunciones son bloques de codigo disenadas para
realizar una tarea especifica.

Cuando queremos realizar la tarea que se ha definido en una funcion
simplemente lo que hay que hacer es "llamar" el nombre de la funcion que
queremos ejecutar.

"Definion de funcion" o "sintaxis general de una funcion"

"""
# palabra reservada "def" + nombre de la funcion + parentesis + 2 puntos
def greeting_paulo():
    """
    Docstring for greeting_paulo

    Esta funcion saluda a Paulo
    """
    print("Hello, Paulo!")

greeting_paulo() 

"""
vamos a hacer una funcion que pida al usuario el first_name, middle_name y last_name

La funcion debe regresar el nombre completo.

"""

# La funcion tiene 3 parametros

def create_full_name(first_name, last_name, middle_name =""):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

user_first_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre: ").strip().lower()
user_last_name = input("Escribe tu apellido: ").strip().lower()

# Argumentos
print(create_full_name(
    user_first_name, 
    user_middle_name, 
    user_last_name))

# Argumentos clave = keyword arguments 
full_name_key = create_full_name(
    last_name = user_last_name,
    first_name = user_first_name,
    middle_name = user_middle_name)


# Argumentos posicionales - Positional Arguments
generated_full_name =create_full_name(
    user_first_name, 
    user_last_name)

print(generated_full_name)

# args, kwargs
# como explorar archivos (diccionarios, .txt, csv)
# args por consola (sys)
# cli - command linear interface
# oop - oriented objects programming
# testing


