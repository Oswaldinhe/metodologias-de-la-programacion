"""
    Tuplas: Las tuplas son listas de elementos que no cambian de tamano.
    Las tuplas son listas inmutables.

    Se utilizan los () para definir una tapla.
    O la palabra reservada tuple().

    Si tenemos un rectangulo que siempre va a tener cierto tamano, podemos asegurar
    que su tamano no va a cambiar si colocamos sus valores en una tupla.

"""
# Ejemplo de tuplas

dimensions = (200,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# dimension[0]=300 #NO SE PUEDE #TypeError

for dimension in dimensions:
    print(dimension)

"""
No podemos modificar una tupla directamente, lo que si podemos hacer es cambiar la asignacion a una variable que almacena
una tupla.
"""
dimensions = (200,50)
print(dimensions)
dimensions = (400,100)
print(dimensions)
