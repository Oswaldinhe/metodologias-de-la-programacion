"""
Centinel is useful when you want to ensure that a loop runs 
at least once befdore checking a condition

Vamos a realizar un ejempo que reaice la suma de 
n numeros ingresados por el usuario,
no sabemos cuantos numeros van a ser, lo que queremos contabilizar
es cuantos numeros se han ingresado y mostrar la suma, el minimo
y el maximo de los numeros ingresados

"""
counter = 0
sum_values = 0.0
minimum = None
maximum = None

while True:
    number = input("Ingrese un numero (o exit para terminar"): ")

    if number == 'exit':
        break
    try:
        number = float(number)
    except ValueError:
        print("Entrada invalida, Por favor, ingrese un numero")
        continue
    sum_values += number
    counter += 1
    
    if minimum is None or number < minimum:
        minimum = number
    if maximum is None or number > maximum:
        maximum = number 

