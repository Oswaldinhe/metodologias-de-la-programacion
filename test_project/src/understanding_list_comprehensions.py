"""
Un list comprehension combna el for loop y la creacion de nuevos elementos en una sola linea automaticamente
agrega cada nuevo elemento a la lista, sin tener que utilizar el metodo append.
"""



# Generar una lista de los cuadrados de los primeros 10 numeros
squares = [value**2 for value in range(1,11)]
print(squares)

evens = [value for value in range(101) if value%2 == 0]
print(evens)