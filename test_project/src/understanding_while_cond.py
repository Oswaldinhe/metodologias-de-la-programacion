"""
Vamos a hacer un programa que escriba un
pin correcto definamos un maximo de intentos y 
el usuario tiene que ingresar el pin correcto

si el pin es correcto mostrmamos un mensaje de bienvenida si el pin es incorrecto mostramos
un mensaje de error.

si el usuario supera el maximo de intentos, mostramos un mensaje de bloqueo

"""



VALID_PIN = "1234"  # UPPER SNAKE CASE 
MAX_ATTEMPTS = 3    # UPPER SNAKE CASE 
attempt = 0

while attempt < MAX_ATTEMPTS:
    user_pin = input("Ingrese su pin: ")
    if user_pin == VALID_PIN:
        print("Bienvenido al sistema.")
        break
    else:
        attempt += 1  
        remaining_attempts = MAX_ATTEMPTS - attempt 
        if remaining_attempts > 0:
            print(f"PIN incorrecto. Te quedan {remaining_attempts} intentos.") 
        else:
            print("Has superado el maximo de intentos. Tu cuenta ha sido bloqueada.")    
            