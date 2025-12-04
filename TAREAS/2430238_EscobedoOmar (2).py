
# Nombre del estudiante: ESCOBEDO CONTRERAS OMAR OSWALDO
# Matrícula : 2430238
# Grupo: 1-1
# Materia: METODOLOGIAS DE LA PROGRAMACION
# Tarea: Tipos numéricos y booleanos 
# LINK DL REPO EN GITHUB: https://github.com/Oswaldinhe/metodologias-de-la-programacion

## RESUMEN EJECUTIVO
"""
En Python, int representa números enteros (sin parte decimal) y
float representa números reales con decimales. Los booleanos (bool)
sólo pueden tomar dos valores: True o False, y normalmente se
obtienen a partir de comparaciones (>, <, ==, etc.) y expresiones
lógicas (and, or, not). Validar rangos y evitar divisiones entre
cero es esencial para prevenir errores de ejecución y resultados
ilógicos. En este archivo se presentan seis problemas que usan int,
float y bool para convertir temperaturas, calcular pagos, aplicar
descuentos, obtener estadísticas, evaluar elegibilidad de préstamos
y clasificar el BMI, incluyendo entradas, salidas, validaciones y
casos de prueba documentados.
"""


## PRINCIPIOS Y BUENAS PRACTICASS (tipos numéricos y booleanos)
"""
- Usar tipos apropiados: int para contadores y cantidades enteras,
  float para cantidades con decimales (salarios, temperaturas, BMI).
- Evitar duplicar expresiones complejas: guardar resultados
  intermedios en variables con nombres claros.
- Validar datos antes de operar (por ejemplo, que horas, salarios
  e ingresos no sean negativos y que divisores no sean cero).
- Usar nombres de variables descriptivos y mensajes claros para el
  usuario para facilitar la lectura del programa.
- Documentar claramente cómo se interpretan los booleanos, es decir,
  qué significa true y qué significa false en cada contexto.
"""


# Función auxiliar para mostrar booleanos
"""
 Esta función convierte un valor booleano de Python (True/False)
 en las cadenas "true" o "false" en minúsculas para mantener
 un formato consistente en las salidas.
 """
def bool_to_str(value):
    return "true" if value else "false"



## Problema 1: Temperature converter and range flag

"""
 Problem 1: Temperature converter and range flag
 Descripción:
 Este programa lee una temperatura en grados Celsius (float) y la
 convierte a Fahrenheit y Kelvin. Además, determina si la temperatura
 en Celsius se considera "alta" (is_high_temperature = true) cuando
 es mayor o igual a 30.0. Si la temperatura en Kelvin resulta
 físicamente imposible (menor que 0.0), se marca como entrada inválida.

 Entradas:
 - temp_c: float, temperatura en °C.

 Salidas:
 - "Fahrenheit:" <temp_f>
 - "Kelvin:" <temp_k>
 - "High temperature:" true|false

 Validaciones:
 - Verificar que temp_c pueda convertirse a float.
 - Verificar que temp_k >= 0.0; si no, mostrar "Error: invalid input".

 Casos de prueba:
 Normal:
 temp_c = 30.0
 temp_f = 86.0, temp_k = 303.15, high = true
 Borde:
 temp_c = -273.15
 temp_k = 0.0 → válido (cero absoluto)
 Error:
 temp_c = -300.0 → temp_k = -26.85 < 0.0
 Salida: Error: invalid input
"""

HIGH_TEMP_THRESHOLD = 30.0

print("=== Problem 1: Temperature converter and range flag ===")
temp_c_text = input("Enter temperature in Celsius: ")

try:
    temp_c = float(temp_c_text)
except ValueError:
    print("Error: invalid input")
else:
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    temp_k = temp_c + 273.15

    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = (temp_c >= HIGH_TEMP_THRESHOLD)
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", bool_to_str(is_high_temperature))


## Problema 2: Work hours and overtime payment

"""
 Problem 2: Work hours and overtime payment
 Descripción:
 Este programa calcula el pago semanal de un trabajador. Hasta 40
 horas se pagan a hourly_rate; las horas extra (> 40) se pagan al
 150% de la tarifa normal. También se genera un booleano has_overtime
 que indica si el trabajador hizo horas extra.

 Entradas:
 - hours_worked: float, horas trabajadas en la semana.
 - hourly_rate: float, pago por hora.
 Salidas:
 - "Regular pay:" <regular_pay>
 - "Overtime pay:" <overtime_pay>
 - "Total pay:" <total_pay>
 - "Has overtime:" true|false

 Validaciones:
 - hours_worked >= 0
 - hourly_rate > 0
 - Si no se cumple, mostrar "Error: invalid input".

 Casos de prueba:
 Normal:
 hours_worked = 45, hourly_rate = 100
 regular_pay = 4000, overtime_pay = 750, total = 4750, has_overtime = true
 Borde:
 hours_worked = 40, hourly_rate = 80
 overtime_pay = 0, has_overtime = false
 Error:
 hours_worked = -5, hourly_rate = 100
 Salida: Error: invalid input
"""

FULL_WEEK_HOURS = 40.0
OVERTIME_RATE_MULTIPLIER = 1.5

print("\n=== Problem 2: Work hours and overtime payment ===")
hours_worked_text = input("Enter hours worked: ")
hourly_rate_text = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_worked_text)
    hourly_rate = float(hourly_rate_text)
except ValueError:
    print("Error: invalid input")
else:
    if hours_worked < 0.0 or hourly_rate <= 0.0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, FULL_WEEK_HOURS)
        overtime_hours = max(hours_worked - FULL_WEEK_HOURS, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_RATE_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > FULL_WEEK_HOURS)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", bool_to_str(has_overtime))



## Problema 3: Discount eligibility with booleans

"""
 Problem 3: Discount eligibility with booleans
 Descripción:
 Este programa determina si un cliente obtiene un descuento del 10%
 en su compra. La regla es:
 - Hay descuento si:
 - is_student es true OR
 - is_senior es true OR
 - purchase_total >= 1000.0
 También calcula el total final a pagar aplicando el descuento cuando
 sea elegible. Las banderas is_student e is_senior se obtienen a partir
 de textos "YES"/"NO" ingresados por el usuario.

 Entradas:
 - purchase_total: float, total de la compra.
 - is_student_text: string, "YES" o "NO".
 - is_senior_text: string, "YES" o "NO".

 Salidas:
 - "Discount eligible:" true|false
 - "Final total:" <final_total>

 Validaciones:
 - purchase_total >= 0.0
 - Textos sólo pueden ser "YES" o "NO" (ignorando mayúsculas/minúsculas).
 - Si no se cumple, mostrar "Error: invalid input".

 Casos de prueba:
 Normal:
 purchase_total = 800, is_student = "YES", is_senior = "NO"
 discount_eligible = true, final_total = 720
 Borde:
 purchase_total = 1000, is_student = "NO", is_senior = "NO"
 discount_eligible = true, final_total = 900
 Error:
 purchase_total = -50
 Salida: Error: invalid input
"""

DISCOUNT_RATE = 0.10
DISCOUNT_MIN_TOTAL = 1000.0

print("\n=== Problem 3: Discount eligibility with booleans ===")
purchase_total_text = input("Enter purchase total: ")
is_student_text = input('Is student? (YES/NO): ')
is_senior_text = input('Is senior? (YES/NO): ')

try:
    purchase_total = float(purchase_total_text)
except ValueError:
    print("Error: invalid input")
else:
    if purchase_total < 0.0:
        print("Error: invalid input")
    else:
        is_student_upper = is_student_text.strip().upper()
        is_senior_upper = is_senior_text.strip().upper()

        if is_student_upper not in ("YES", "NO") or is_senior_upper not in ("YES", "NO"):
            print("Error: invalid input")
        else:
            is_student = (is_student_upper == "YES")
            is_senior = (is_senior_upper == "YES")

            discount_eligible = is_student or is_senior or (purchase_total >= DISCOUNT_MIN_TOTAL)

            if discount_eligible:
                final_total = purchase_total * (1.0 - DISCOUNT_RATE)
            else:
                final_total = purchase_total

            print("Discount eligible:", bool_to_str(discount_eligible))
            print("Final total:", final_total)



## Problema 4: Basic statistics of three integers

"""
 Problem 4: Basic statistics of three integers
 Descripción:
 Este programa lee tres números enteros y calcula su suma, el promedio
 (como float), el valor máximo, el valor mínimo y un booleano all_even
 que indica si los tres números son pares.

 Entradas:
 - n1: int
 - n2: int
 - n3: int

 Salidas:
 - "Sum:" <sum_value>
 - "Average:" <average_value>
 - "Max:" <max_value>
 - "Min:" <min_value>
 - "All even:" true|false

 Validaciones:
 - Verificar que los tres valores se puedan convertir a int.
 - Se permiten valores negativos; no hay restricciones adicionales.

 Casos de prueba:
 Normal:
 n1 = 2, n2 = 4, n3 = 6
 sum = 12, average = 4.0, max = 6, min = 2, all_even = true
 Borde:
 n1 = 1, n2 = 2, n3 = 3
 sum = 6, average = 2.0, max = 3, min = 1, all_even = false
 Error:
 n1 = "a", n2 = 2, n3 = 3
 Salida: Error: invalid input
"""

print("\n=== Problem 4: Basic statistics of three integers ===")
n1_text = input("Enter first integer: ")
n2_text = input("Enter second integer: ")
n3_text = input("Enter third integer: ")

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)
except ValueError:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", bool_to_str(all_even))


## Problema 5: Loan eligibility (income and debt ratio)

"""
 Problem 5: Loan eligibility (income and debt ratio)
 Descripción:
 Este programa determina si una persona es elegible para un préstamo
 en función de su ingreso mensual, deuda mensual y puntaje de crédito.
 Se calcula la razón de deuda (debt_ratio = monthly_debt / monthly_income)
 y se considera elegible si:
 - monthly_income >= 8000.0 AND
 - debt_ratio <= 0.4 AND
 - credit_score >= 650

 Entradas:
 - monthly_income: float, ingreso mensual.
 - monthly_debt: float, pagos mensuales de deuda.
 - credit_score: int, puntaje de crédito.

 Salidas:
 - "Debt ratio:" <debt_ratio>
 - "Eligible:" true|false

 Validaciones:
 - monthly_income > 0.0 (para evitar división entre cero o valores no válidos).
 - monthly_debt >= 0.0
 - credit_score >= 0
 - Si no se cumple, mostrar "Error: invalid input".

 Casos de prueba:
 Normal:
 monthly_income = 10000, monthly_debt = 3000, credit_score = 700
 debt_ratio = 0.3, eligible = true
 Borde:
 monthly_income = 8000, monthly_debt = 3200, credit_score = 650
 debt_ratio = 0.4, eligible = true
 Error:
 monthly_income = 0, monthly_debt = 1000, credit_score = 700
 Salida: Error: invalid input
"""

MIN_INCOME_FOR_LOAN = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

print("\n=== Problem 5: Loan eligibility (income and debt ratio) ===")
monthly_income_text = input("Enter monthly income: ")
monthly_debt_text = input("Enter monthly debt: ")
credit_score_text = input("Enter credit score: ")

try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)
except ValueError:
    print("Error: invalid input")
else:
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= MIN_INCOME_FOR_LOAN
            and debt_ratio <= MAX_DEBT_RATIO
            and credit_score >= MIN_CREDIT_SCORE
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", bool_to_str(eligible))



## Problema 6: Body Mass Index (BMI) and category flag

"""
Problem 6: Body Mass Index (BMI) and category flag
Descripción:
Este programa calcula el índice de masa corporal (BMI) de una persona
usando la fórmula:
 - bmi = weight_kg / (height_m * height_m)
 Luego genera tres banderas booleanas:
 - is_underweight (bmi < 18.5)
 - is_normal (18.5 <= bmi < 25.0)
 - is_overweight (bmi >= 25.0)

 Entradas:
 - weight_kg: float, peso en kilogramos.
 - height_m: float, estatura en metros.

 Salidas:
 - "BMI:" <bmi_redondeado>
 - "Underweight:" true|false
 - "Normal:" true|false
 - "Overweight:" true|false

 Validaciones:
 - weight_kg > 0.0
 - height_m > 0.0
 - Si no se cumple, mostrar "Error: invalid input".

 Casos de prueba:
 Normal:
 weight_kg = 70, height_m = 1.75 → bmi ≈ 22.86
 Underweight = false, Normal = true, Overweight = false
 Borde:
 weight_kg = 50, height_m ≈ 1.65 → bmi ≈ 18.37
 Underweight = true, Normal = false
 Error:
 weight_kg = -60, height_m = 1.7
 Salida: Error: invalid input
"""

print("\n=== Problem 6: Body Mass Index (BMI) and category flag ===")
weight_kg_text = input("Enter weight in kg: ")
height_m_text = input("Enter height in meters: ")

try:
    weight_kg = float(weight_kg_text)
    height_m = float(height_m_text)
except ValueError:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = (bmi >= 18.5) and (bmi < 25.0)
        is_overweight = bmi >= 25.0

        print("BMI:", bmi_rounded)
        print("Underweight:", bool_to_str(is_underweight))
        print("Normal:", bool_to_str(is_normal))
        print("Overweight:", bool_to_str(is_overweight))



## CONCLUSIONES
"""
En estos seis problemas se mostró cómo los enteros y flotantes
trabajan juntos en cálculos reales como temperaturas, salarios,
razones de deuda y BMI. Las comparaciones numéricas generan
booleanos que permiten tomar decisiones mediante estructuras if,
activando banderas como is_high_temperature o eligible. La
validación de rangos y la prevención de divisiones entre cero
resultaron fundamentales para evitar errores lógicos. El uso de
operadores lógicos and, or y not permitió combinar condiciones en
escenarios de descuentos, horas extra y préstamos. Estos mismos
patrones se repiten en aplicaciones reales de nómina, sistemas de
ventas, análisis financiero y evaluación de riesgos.
"""

## Referencias


# References:
# https://www.youtube.com/watch?v=aSqWmjDIwG8
# (int, float, complex)". Python Documentation, https://docs.python.org/
# https://www.youtube.com/watch?v=DeZiP2vCY4M
# Operations". Python Documentation, https://docs.python.org/
#  Python Software Foundation. "Expressions — Arithmetic, Comparison and Boolean operators". Python Documentation.
# https://www.youtube.com/watch?v=bvU345BIioI
# Apuntes de clase y material del curso sobre operadores aritméticos, relacionales, lógicos y validación de datos numéricos en Python.
