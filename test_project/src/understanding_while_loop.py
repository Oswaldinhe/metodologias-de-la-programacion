"""

      Estructura basica del bucle while

      conditional -> bool

      while conditional:
        actions
"""

# Estructura try: except:


# While infinito


while True: # While infinito
 try: 
      number = int(input("Escribe un numero entre 25 y 50: "))
      if number >= 25 and number <= 50:
            print("Hola estas dentro del rango")
            break
      else:
            print("Lastima margarito, escribe otro numero")

 except ValueError:
     print("Caracter invalido")
 except KeyboardInterrupt:
  print("\nPrograma finalizado por el usuario.")
  break





# While con centinela