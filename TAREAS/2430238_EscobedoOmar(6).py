
# Portada

# Nombre del estudiante: ESCOBEDO CONTRERAS OMAR OSWALDO
# Matrícula (student ID): 2430238
# Grupo: 1-1 IM
# Materia: Introducción a la Programación con Python
# Tarea: Generador de serie de Fibonacci
# Fecha: 2025-12-05
# LINK DL REPO EN GITHUB: https://github.com/Oswaldinhe/metodologias-de-la-programacion

# Resumen ejecutivo
"""
 La serie de Fibonacci es una sucesión de números donde cada término
 (a partir del tercero) es la suma de los dos anteriores, empezando
 típicamente en 0 y 1. Calcular la serie hasta un número de términos n
 significa generar los primeros n valores de esa sucesión. Este programa
 lee un entero n, valida que sea un número de términos válido y luego
 genera la serie usando un bucle. Finalmente, muestra los términos en
 una sola línea de salida.
"""



# Documentación del problema

# Problem: Fibonacci series generator
# Description:
"""
 Program that reads an integer n and prints the first n terms of the
 Fibonacci series starting at 0 and 1. The program validates the input
 anduses a loop to generate the sequence.
"""
"""
 Inputs:
 - n (int; number of terms to generate)

 Outputs:
 - Optional: "Number of terms:" followed by n
 - "Fibonacci series:" followed by the n terms separated by spaces

 Validations:
 - n must be an integer
 - n must be >= 1
 - n must be <= 50 (maximum limit to avoid very large series)
 - If validation fails, print "Error: invalid input" and do not
   calculate the series.

 Test cases:
 1) Normal:
    n = 7
    Expected output:
    Number of terms: 7
    Fibonacci series: 0 1 1 2 3 5 8

 2) Border:
    n = 1
    Expected output:
    Number of terms: 1
    Fibonacci series: 0

 3) Error:
    n = 0  (or n = 51)
    Expected output:
    Error: invalid input   
"""
"""
 Diagrama de flujo (descripción en texto - opcional):
 1) Leer n como texto.
 2) Intentar convertir n a entero.
 3) Validar que 1 <= n <= 50.
 4) Si es inválido, mostrar mensaje de error.
 5) Si es válido, generar la serie de Fibonacci desde 0 y 1 usando
    un bucle y variables para los términos actuales.
 6) Imprimir la serie en una sola línea.
"""

# Código del problema: Fibonacci series up to n terms


MAX_TERMS = 50  # límite máximo opcional para n

n_text = input("Enter number of terms: ")

# Validación de entrada: conversión a int
try:
    terms_count = int(n_text)
except ValueError:
    print("Error: invalid input")
else:
    # Validación de rango
    if terms_count < 1 or terms_count > MAX_TERMS:
        print("Error: invalid input")
    else:
        # Generación de la serie de Fibonacci
        # La serie comienza en 0 y 1.
        fibonacci_series = []
        if terms_count >= 1:
            fibonacci_series.append(0)
        if terms_count >= 2:
            fibonacci_series.append(1)

        # Usamos un bucle for para generar los términos restantes
        for _ in range(2, terms_count):
            next_term = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_term)

        # Impresión de resultados
        print("Number of terms:", terms_count)
        # Convertimos los enteros a cadenas para unirlos con espacios
        terms_as_strings = [str(term) for term in fibonacci_series]
        print("Fibonacci series:", " ".join(terms_as_strings))



# Conclusiones
"""
 El uso de un bucle permitió generar la serie de Fibonacci de forma
 iterativa, reutilizando el mismo patrón de suma entre términos
 consecutivos. Manejar correctamente los casos especiales n = 1 y
 n = 2 asegura que la salida sea coherente con la definición de la
 serie desde 0 y 1. La validación previa de la entrada evita errores
 por valores negativos o fuera del rango establecido. Esta misma
 lógica podría reutilizarse en otros programas que necesiten calcular
 esta serie para análisis numéricos, gráficos o ejemplos didácticos.
"""



# References:
"""
 1) Python Software Foundation. "The for statement" and "The while
    statement". Python Documentation, https://docs.python.org/
 2) TutorialsPoint / W3Schools. "Python Program to Print Fibonacci
    Sequence". Tutoriales introductorios de Python.
 3) Apuntes de clase y materiales del curso sobre bucles, variables
    y ejemplos de la serie de Fibonacci en Python.
"""""