# Numbers - Numericos enteros

"""

Integers

Los podemos sumar (+), restar (-),
multiplicar (*), dividir (/),
elevar a una potencia (**2, **3, ...., etc)
obtener el modulo (%)

"""
number_1 = 35
number_2 = 15
sum = number_1+number_2
mult = number_1*number_2
cocient = number_1/number_2
difference = number_1-number_2
power = number_1**2
modulo = number_1%number_2

print("Sum:", sum,  type(sum))
print("difference:", difference, type(difference))
print("multiplication:", mult, type(mult))
print("cocient:", cocient, type (cocient))
print("power:", power, type (power))
print("modulo:", modulo, type (modulo))

"""

Python respeta la Jerarquia de operaciones

2+3*4 = 14
(2+3)*4 = 20

"""

# Floats 
"""
Floats

Los podemos sumar (+), restar (-),
multiplicar (*), dividir (/),
elevar a una potencia (**2, **3, ...., etc)

Python llama floats a cualquier numero con un punto decimal.

"""
print("floats")
print (0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(0.1*2)


"""
Tomar en cuenta que en ocasiones podemos obtener un numero arbitrario de numeros decimales en la respuesta.
Esto pasa en muchos lenguajes de programacion, pero no nos debemos preocupar :).

"""

print(0.2+0.1)
print(3*0.1)


# Imprimir la edad de alguien 
age = 33
message = "Charly tiene " + str(age) + " años."
print(message)

"""
TypeError: Pasa cuando Python no puede reconocer el tipo de informacion que se esta utilizando.

Buil-in Method
str()

"""
message_f = f"Charly tiene {age} años."
print(message_f)

