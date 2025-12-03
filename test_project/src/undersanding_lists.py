# LISTAS
"""
Las listas  nos permiten almacenar informacion en un lugar, 'la cantidad que tengas': ya sean
pocos elementos o millones de elementos.

Se recomienda nombrar una variable del tipo lista en PLURAL.

En Python los corchetes[] indican o definen una lista, los elementos en una lista se separan por comas.

Ejemplo:
"""
# Definiciones de una lista
bicycles = ['trek', 'cannondale', "redline", "giant",]
print(bicycles, type(bicycles))

# Acceder a lementos de una lista
print(bicycles[0].title(), type(bicycles[0]))
print(bicycles[3].title(), type(bicycles[3]))

# Acceder al ultimo elemento de la lista 
print(bicycles[-1].title(), type(bicycles[-1]))
print(bicycles[-2].title(), type(bicycles[-2]))
print(bicycles[-4].title(), type(bicycles[-4]))

message = "my first bicycle was a " + bicycles[0].title()+ "."
print(message)


motorcycles = ["honda", "yamaha", "suzuki"]
print("lista original: ", motorcycles)

motorcycles.append("ducati")
print("Lista append: ", motorcycles)

"""
El metodo append() agrega elementos 
al final de una lista.

"""

# Crear una lista vacia y luego agregar elementos
cars = []
print("lista de carros: ", cars)
cars.append("bmw")
print("lista de carros: ", cars)
cars.append("audi")
print("lista de carros: ", cars)
cars.append("toyota")
print("lista de carros: ", cars)

# Agregar elementos en una posicion especifica
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(3, "ducati")
print("lista de motocicletas: ", motorcycles)

# Eliminar elementos de una lista usando del
print("Lista original de motocicletas: ", motorcycles)
del motorcycles[0]
print("Lista de motocicletas despues de eliminar el primer elemento: ", motorcycles)
print("-----------------------------POP----------------------------------------------")

# Eliminar un elemento usando el metodo pop()
print("lista original de motocicletas: ", motorcycles)
popped_motorcycle = motorcycles.pop()
print("Lista de motocicletas despues de usar pop(): ", motorcycles)
print("Motocicleta eliminada: ", popped_motorcycle)

print("-----------------------------POP------INDICE----------------------------------------")
print("lista original de motocicletas: ", motorcycles)
# Usar pop() para eliminar un elemento en una posicion especifica
second_motorcycle = motorcycles.pop(1)
print("Lista de motocicletas despues de usar pop(): ",motorcycles)
print("Motocicleta eliminada: ", second_motorcycle)

# Eliminar elementos de una lista por valor 

"""
motorcycles.remove(ducati)
  print(motorcycles) [] 
"""

# Ordenar listas
# Permanentemente metodo .sort()
# .sort(reverse=true) ordenara al reves

cars = ['bmw', 'kia', 'ford', 'toyoya']
cars.sort()
print(cars) # ['bmw', 'ford', 'kia', 'toyota']
print(len(cars)) # cantidad de elementos en la lista


# Hacer lista de lo que sea

numeros_favoritos = [1,7,15,23] 
print(numeros_favoritos)
(numeros_favoritos.reverse())
print(numeros_favoritos)

# numeros_favoritos.sort(reverse=True) es opcional el reverse = true
# print(numeros_favoritos)






























