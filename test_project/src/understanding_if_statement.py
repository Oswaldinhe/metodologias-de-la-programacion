cars = ['audi','bmw','volvo','tesla','toyota']
for car in cars:
    if car=='bmw' or car=='tesla':
        print(car.upper())
    else:
        print(car.lower())


# El condicional es el corazon de un if
# Ejemplos de condicionales

# Conditional True
car_1 = 'bmw'
print("Conditional True: ",car_1=='bmw')

# Confitional Fakse
car_2 = 'Audi'
print("Conditional False: ",car_1=='audi')

car_3 = 'Audi'
print(car_3.lower()=='audi')

# Conditional != para determinar desigualdad
requested_toppin = 'mushrooms'
if requested_toppin != 'anchovies':
    print('Hold the anchovies')                                        


# Comparaciones numericas
age = 18
print(age==18) # True

answer = 17
if answer != 42: # True
    print("Esa no es la respuesta correcta. Intente otra vez por favor")

age = 19
print(age<21) # True
print(age<=21) # True
print(age>21) # False
print(age>=21) # False

# Condicionales multiples

age_0 = 22
age_1 = 18

# Operacion logica and
print(age_0>=21 and age_1>21) # False
print(age_0>=21 and age_1>=18) # True

# Operacion logica or 
print(age_0>=22 or age_1>21) # True
print(age_0>=23 or age_1>=21) # False

# Preguntarme si un valor esta en una lista
cars = ["micro","vocho","tsuru","tsubaru"]
print("vocho" in cars)
print("chevy" in cars)

# Preguntarnos si un valor no esta en una lista

aumnos = ["victor","ana","maiki","gera"]
user = 'josue'

####  print(user not in alumnos)  # True
#### print('maiki' not in alumnos)  # False

# Datos booleanos
game_active =True
can_edit = False


# If statement

"""
Programa para pedir la edad a un usuario que diga si
el usuario es menor de edad o mayor de edad

"""


age = 0
# try: except:

try:
    age = int(input("Dime tu edad: "))

    
except Exception as err:
    age = -1

# if-elif-else
if (age) >= 18 and age <= 100 :
    print("Eres mayor de edad")
elif age<18 and age > 0:
    print("Eres menor de edad")
elif age>100:
    print("Tienes mas de un siglo vivo cawn")     
else:
    print("Cometiste un error")           
    
   

print("Hola Charly")   


"""
Ejercicio:

    Elabore un programa que contemple lo siguiente:
    -Si la edad es menor de 4 aanos, la entrada es gratuita
    -Si la edad esta dentro de (4 y 18] anos (inclusivo), el costo es de $200
    - Costo para alguien mayor de 18, $500
"""
age_2 = 0

try:
    age = int(input("Enter your age please: "))

except Exception as error:
    age_2 = -1

if age_2 >4 and age <= 18:
    print("Pay your $200 bill please")
elif age_2<4:
     print("You have frepass") 
elif age_2>18:
    print("Pay your $500 bll please")
        
else:
    print("Cometiste un error")        


# multiple if-elf-else blocks
# else en ocasiones se puede omitir (depende de la situacion)
# como se va ejecutando el if-elif-else

## Multiple condition

print("\n Guisos en bloque if-elif-else")
guisos = ["deshebrada", "salsa verde","picadillo"]
if "deshebrada" in guisos:
    print("hay deshebrada".upper())
else:
    print("no hay deshebrada".upper())    

if "picadillo" in guisos:
    print("hay picadillo".swapcase())  
else:
    print("no hay picadillo".swapcase())    
if "salsa verde" in guisos:
    print("hay salsa verde".title())
else:
    print("no hay salsa verde".title())    
if "mole" in guisos:
    print("Hay mole")    
else:
    print("No hay mole")    


# Listas vacias
guisos = [] # Lista vacia
if guisos:
    print("Hay guisos")
else: 
    print("No hay guisos")    

## Utilizando dos listas
guisos_disponibles = ["salsa verde","deshebrada","picadillo"]
guisos_a_ordenar = ["barbacoa","deshebrada","cabrito"]

print("¿Que guiso desea ordenar?")
for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print(f"Si tenemos {guiso}")
    else:
        message_no_guiso = f"""
    Cafeteria Jaguares
        No tenemos {guiso}
        """
        print(message_no_guiso)


print("Realizando pedido")           

