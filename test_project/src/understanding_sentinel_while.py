# While con sentinela
"""
 Sumar n numeros hasta que el usuario escriba la palabra exit.
Tambien vamos a decir cuantos numeros ingreso el usuario.
Cual es el minimo y cual es el maximo.
"""
print("\n Captura de importes. Bienvenidos a la calculadora de PAULO")
print("Para salir en cualquier momento ingresa la palabra 'exit'")
counter = 0
sum = 0.0
maximum = None
minimum = None

while True:

    user_input = input("Ingresa una cantidad (MXN): ")

    if user_input == "exit":
        break

    try:
        quantity = float(user_input)
    except:
        print("Ingresa un valor valido")
        continue 

    counter+=1  #counter = counter + 1 (contador)
    sum+=quantity # sum = sum + quantity (acumulador)

    if minimum is None or quantity < minimum:
        minimum = quantity
    if maximum is None or quantity > maximum:
        maximum = quantity


print(sum)
print(minimum)
print(maximum)
print(counter)
       