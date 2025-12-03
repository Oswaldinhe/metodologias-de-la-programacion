# LOOPING (LOOP)
magicians = ["harry","ron","hermione", "jorge"]
print(magicians[0], magicians[1],magicians[2],magicians[3])
print("\n")

"""
iterable: te dice cuantos elementostiene una estructura for iterable=
<----4 espacios y despues las acciones

"""
for magician in magicians:
    print(magician)
    print(magician.upper())
    print("\n")

"""
Identificacions: Python utiliza la identacion para determinar cuando una linea de codigo esta conectada a la linea de codigo anterior.
Basicamente, se utilizan 4 espacios en blanco para obligarnos a escribir codigo ordenado y estructurado.

"""
for magician in magicians:
    print(magician)
    print(f"Gracias{magician.upper()}fue un gran espectaculo")

# IDENTACION INNECESARIA
"""
print("Hola Charly")
print("Como estas")
"""
# FOR

