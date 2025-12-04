
# Nombre del estudiante: Escobedo Contreras Omar Oswaldo
# Matrícula: 2430238
# Grupo: 1-1
# Materia: METODOLOGIAS DE LA PROGEAMACION 
# LINK DL REPO EN GITHUB: https://github.com/Oswaldinhe/metodologias-de-la-programacion


## RESUMEN EJECUTIVO 
"""
 En Python, un string (str) es una secuencia de caracteres inmutable,
 lo que significa que no puede modificarse en el lugar: cualquier
 “cambio” genera una nueva cadena. Sobre los strings se pueden realizar
 operaciones como concatenar, obtener su longitud, extraer subcadenas
 (slicing), buscar patrones, reemplazar texto y dividir/unir palabras.
 Es importante validar y normalizar el texto de entrada (por ejemplo,
 correos, nombres y contraseñas) usando métodos como strip() y lower()
 antes de compararlo. Este archivo presenta seis problemas que usan
 métodos de string para formatear nombres, validar correos, revisar
 palíndromos, analizar oraciones, clasificar contraseñas y formatear
 etiquetas, incluyendo validaciones y casos de prueba.
 """

"""
 Los strings son inmutables: cualquier operación que parezca
 modificarlos realmente devuelve una nueva cadena.
 Es buena práctica normalizar entradas con strip() (quitar espacios
 externos) y lower() antes de compararlas.
 Evitar “números mágicos” en índices; documentar qué extrae cada
 slice y por qué se usan esos valores.
 Usar métodos de string (lower, upper, split, join, replace, etc.)
 en lugar de reescribir lógica básica de manipulación de texto.
 Diseñar validaciones claras: primero verificar que la entrada no
 esté vacía y después revisar el formato.
 Escribir código legible: nombres de variables claros y mensajes de
 error entendibles para el usuario.
 """

 

## PRINCIPIOS Y BUENAS PRACTICASS


## Problema 1: Full name formatter (name + initials)

"""
 Dado el nombre completo de una persona en una sola cadena, este
 programa normaliza espacios y mayúsculas/minúsculas, y muestra el
 nombre en Title Case y las iniciales. Por ejemplo, a partir de
 "juan   carlos tovar" se debe imprimir "Juan Carlos Tovar" y
 "J.C.T." como iniciales.


 Inputs:
 - full_name (string; nombre completo, puede incluir espacios extra
   y mezcla de mayúsculas/minúsculas).

 Outputs:
 - "Formatted name: <Name In Title Case>"
 - "Initials: <X.X.X.>"

 Validations:
 - full_name no debe estar vacío después de strip().
 - Debe contener al menos dos palabras (nombre y apellido).

 Test cases:
  Normal:
    full_name = "juan carlos tovar"
    -> Formatted name: Juan Carlos Tovar
       Initials: J.C.T.
  Border:
    full_name = "   MARIA   LOPEZ  "
    -> Formatted name: Maria Lopez
       Initials: M.L.
  Error:
    full_name = "   "
    -> Error: invalid input

"""

full_name = input("Enter full name: ")

full_name_stripped = full_name.strip()

if full_name_stripped == "":
    print("Error: invalid input")
else:
    words = full_name_stripped.split()
    if len(words) < 2:
        print("Error: invalid input")
    else:
        # Normalizamos espaciado y título
        normalized_full_name = " ".join(words)
        formatted_name = normalized_full_name.title()

        # Construimos iniciales
        initials_parts = []
        for word in words:
            initials_parts.append(word[0].upper() + ".")
        initials = "".join(initials_parts)

        print("Formatted name:", formatted_name)
        print("Initials:", initials)


## Problema 2: Simple email validator (structure + domain)
"""
 Descripción:
 Este programa valida si una dirección de correo electrónico cumple
 un formato básico:
 - Contiene exactamente un '@'.
 - Después del '@' debe haber al menos un '.'.
 - No contiene espacios en blanco.
 Si el correo es válido, también muestra el dominio (parte después
 de '@').

 Inputs:
 - email_text (string).

 Outputs:
 - "Valid email: true" o "Valid email: false"
 - Si es válido: "Domain: <domain_part>"

 Validations:
 - email_text no vacío tras strip().
 - No debe contener espacios.

 Test cases:
 Normal:
    email_text = "user@example.com"
    -> Valid email: true
       Domain: example.com
  Border:
    email_text = "u@sub.domain.org"
    -> Valid email: true
       Domain: sub.domain.org
  Error (formato):
    email_text = "user@@example.com"
    -> Valid email: false

"""

email_text = input("Enter email: ")

email_text_stripped = email_text.strip()

if email_text_stripped == "":
    print("Error: invalid input")
else:
    # No se permiten espacios
    if " " in email_text_stripped:
        is_valid_email = False
    else:
        at_count = email_text_stripped.count("@")
        if at_count != 1:
            is_valid_email = False
        else:
            at_index = email_text_stripped.find("@")
            domain_part = email_text_stripped[at_index + 1:]
            # Debe haber al menos un punto en el dominio
            is_valid_email = "." in domain_part and domain_part != "."

    if is_valid_email:
        print("Valid email: true")
        print("Domain:", domain_part)
    else:
        print("Valid email: false")



## Problema 3: Palindrome checker (ignoring spaces and case)
"""
 Descripción:
 Este programa determina si una frase es un palíndromo, es decir, se
 lee igual de izquierda a derecha y de derecha a izquierda, ignorando
 espacios y mayúsculas/minúsculas.

 Inputs:
 - phrase (string).

 Outputs:
 - "Is palindrome: true" o "Is palindrome: false"
 - Opcional: "Normalized phrase: <...>"

 Validations:
 - phrase no vacía tras strip().
 - Longitud mínima de la versión normalizada (sin espacios) >= 3.

 Test cases:
  Normal:
    phrase = "Anita lava la tina"
    -> Is palindrome: true
  Border:
    phrase = "oso"
    -> Is palindrome: true
  Error:
    phrase = "   "
    -> Error: invalid input

"""

phrase = input("Enter phrase: ")

phrase_stripped = phrase.strip()

if phrase_stripped == "":
    print("Error: invalid input")
else:
    # Normalizamos: minúsculas y sin espacios
    normalized_phrase = phrase_stripped.lower().replace(" ", "")
    if len(normalized_phrase) < 3:
        print("Error: invalid input")
    else:
        reversed_phrase = normalized_phrase[::-1]
        is_palindrome = (normalized_phrase == reversed_phrase)

        print("Normalized phrase:", normalized_phrase)
        print("Is palindrome:", "true" if is_palindrome else "false")



## Problema 4: Sentence word stats (lengths and first/last word)
"""
 Descripción:
 Dada una oración, este programa:
  Normaliza espacios al principio y al final.
  Separa las palabras por espacios.
  Muestra:
    - Número total de palabras.
    - Primera palabra.
    - Última palabra.
    - Palabra más corta y más larga (por longitud).

 Inputs:
 - sentence (string).

 Outputs:
 - "Word count: <n>"
 - "First word: <...>"
 - "Last word: <...>"
 - "Shortest word: <...>"
 - "Longest word: <...>"

 Validations:
 - sentence no vacía tras strip().
 - Debe contener al menos una palabra después de split().

 Test cases:
  Normal:
    sentence = "Python is very powerful"
    -> Word count: 4
       First word: Python
       Last word: powerful
       Shortest word: is
       Longest word: powerful
  Border:
    sentence = "   hello   "
    -> Word count: 1
       First/Last/Shortest/Longest: hello
  Error:
    sentence = "    "
    -> Error: invalid input
"""
sentence = input("Enter sentence: ")

sentence_stripped = sentence.strip()

if sentence_stripped == "":
    print("Error: invalid input")
else:
    words = sentence_stripped.split()
    if len(words) == 0:
        print("Error: invalid input")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        # Encontrar palabra más corta y más larga
        shortest_word = words[0]
        longest_word = words[0]

        for word in words[1:]:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word

        print("Word count:", word_count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)



## Problema 5: Password strength classifier
"""
 Descripción:
 Este programa clasifica una contraseña como "weak", "medium" o
 "strong" según reglas mínimas:
 - Weak:
   - longitud < 8, o
   - longitud >= 8 pero sólo letras minúsculas (sin dígitos, sin
     mayúsculas, sin símbolos).
 - Strong:
   - longitud >= 8 y contiene al menos:
     - una letra mayúscula,
     - una letra minúscula,
     - un dígito,
     - un símbolo no alfanumérico.
 - Medium:
   - longitud >= 8 y no entra en weak ni en strong, es decir, mezcla
     parcial de tipos de caracteres.

 Inputs:
 - password_input (string).

 Outputs:
 - "Password strength: weak"
 - "Password strength: medium"
 - "Password strength: strong"

 Validations:
 - Contraseña no vacía tras strip().

 Test cases:
  Normal:
    password_input = "Abc123!@"
    -> Password strength: strong
  Border:
    password_input = "password1"
    -> Password strength: medium
  Error:
    password_input = "   "
    -> Error: invalid input

"""
password_input = input("Enter password: ")

password_stripped = password_input.strip()

if password_stripped == "":
    print("Error: invalid input")
else:
    length = len(password_stripped)

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password_stripped:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_symbol = True

    if length < 8:
        password_strength = "weak"
    else:
        # Sólo minúsculas (sin dígitos, sin mayúsculas, sin símbolos)
        if has_lower and not has_upper and not has_digit and not has_symbol:
            password_strength = "weak"
        elif has_upper and has_lower and has_digit and has_symbol:
            password_strength = "strong"
        else:
            password_strength = "medium"

    print("Password strength:", password_strength)



## Problema 6: Product label formatter (fixed-width text)

"""
 Descripción:
 Dado el nombre de un producto y su precio, este programa genera una
 etiqueta en una sola línea con el siguiente formato:
   Product: <NAME> | Price: $<PRICE>
 La cadena completa debe tener exactamente 30 caracteres:
 - Si es más corta, se rellena con espacios al final.
 - Si es más larga, se recorta a 30 caracteres.

 Inputs:
 - product_name (string).
 - price_value (string o número, convertido a float para validar).

 Outputs:
 - "Label: <exactly 30 characters>"
   (Se muestra entre comillas para visualizar los espacios).

 Validations:
 - product_name no vacío tras strip().
 - price_value convertible a número positivo.

 Test cases:
  Normal:
    product_name = "Notebook", price_value = 25.5
    -> Label: "Product: NOTEBOOK | Price: $25.50"
       (recortada o rellenada hasta 30 caracteres)
  Border:
    product_name = "A", price_value = 1
    -> etiqueta corta que se rellena con espacios
  Error:
    product_name = "   ", price_value = 10
    -> Error: invalid input

"""
FIXED_LABEL_LENGTH = 30

product_name = input("Enter product name: ")
price_value_text = input("Enter price: ")

product_name_stripped = product_name.strip()

if product_name_stripped == "":
    print("Error: invalid input")
else:
    try:
        price_value = float(price_value_text)
    except ValueError:
        print("Error: invalid input")
    else:
        if price_value <= 0.0:
            print("Error: invalid input")
        else:
            # Convertimos nombre a mayúsculas en la etiqueta
            product_name_upper = product_name_stripped.upper()
            price_as_text = f"{price_value:.2f}"

            base_label = f"Product: {product_name_upper} | Price: ${price_as_text}"

            if len(base_label) < FIXED_LABEL_LENGTH:
                padding = " " * (FIXED_LABEL_LENGTH - len(base_label))
                final_label = base_label + padding
            else:
                final_label = base_label[:FIXED_LABEL_LENGTH]

            # Mostramos entre comillas para visualizar espacios finales
            print('Label:', f'"{final_label}"')


## CONCLUSIONES
"""
 El manejo de strings es esencial en la entrada y salida de datos,
 ya que la mayoría de la información llega como texto (nombres,
 correos, contraseñas, etiquetas). Métodos como lower(), strip(),
 split() y join() permiten normalizar, separar y reconstruir cadenas
 de manera flexible. Normalizar texto antes de compararlo evita
 errores por diferencias de espacios o mayúsculas/minúsculas. Diseñar
 validaciones claras ayuda a rechazar datos vacíos o con formato
 incorrecto, mejorando la robustez del programa. La inmutabilidad
 de los strings obliga a pensar en términos de “nuevas cadenas” al
 modificar contenido, y los slices facilitan extraer subcadenas sin
 alterar el original.
"""

## Referencias


#  https://www.youtube.com/watch?v=Ctqi5Y4X-jA
#  https://www.youtube.com/watch?v=tb6EYiHtcXU
#  https://www.youtube.com/watch?v=Pr-9wkSJDJk&t=112s
#  Apuntes de clase 
