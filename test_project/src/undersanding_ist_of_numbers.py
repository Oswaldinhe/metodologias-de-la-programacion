"""

Las listas tambien almacenar numeros y de hecho son ideales para eso. 
Python ofrece muchas herramientas que ayudan a trabajar de manera eficiente las lisyas de numeros.

"""
# Metodo range()
# Nos ayuda a generar facilmente series de numeros
# Ejemplo: 

print("imprime los primeros 10 numeros")
for number in range(10):
    print(number)

first_10_numbers = list(range(10))
print (first_10_numbers)


print("imprime los numeros del 1 al 4")
for number in range(1,5):
    print(number)
first_4_numbers = list(range(1,5))
print (first_4_numbers)


print("imprime los numeros pares entre el 0 y el 10")
for number in range(0,11,2):
    print(number)
first_even_numbers = list(range(0,11,2))
print (first_even_numbers)


print("imprime los numeros impares entre el 0 y el 10")
for number in range(1,11,2):
    print(number)
first_odd_numbers = list(range(1,11,2))
print (first_odd_numbers)

print("imprime la tabla del 5")
for number in range(0,51,5):
    print(number)
tabla_del_5 = list(range(5,51,5))
print(tabla_del_5)


print("Generar una lista con los cuadrados de los primeros 10 numeros")
squares = []
for number in range(1,11):
     square = number**2
     squares.append(square)
print(squares)


#### Otros metodos built-in
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) # salida 0
print(max(digits)) # salida 9
print(sum(digits)) # salida 45
