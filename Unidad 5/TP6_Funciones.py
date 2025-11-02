def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' por pantalla."""
    print("Hola Mundo!")

# Llamada desde el programa principal
print("--- Ejercicio 1 ---")
imprimir_hola_mundo()

def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y devuelve un saludo personalizado.
    """
    return f"Hola {nombre}!"

# Llamada desde el programa principal
print("\n--- Ejercicio 2 ---")
# Solicitamos el nombre al usuario
nombre_usuario = input("Ingresá tu nombre: ")
# Llamamos a la función y guardamos el saludo que devuelve
saludo_personalizado = saludar_usuario(nombre_usuario)
print(saludo_personalizado)

def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe cuatro parámetros e imprime un mensaje formateado.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Pedir los datos al usuario
print("\n--- Ejercicio 3 ---")
nombre_ingresado = input("Ingresá tu nombre: ")
apellido_ingresado = input("Ingresá tu apellido: ")
edad_ingresada = input("Ingresá tu edad: ")
residencia_ingresada = input("Ingresá tu lugar de residencia: ")

# Llamar a la función con los valores ingresados
informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)

# Importamos la librería 'math' para usar el valor de Pi
import math

def calcular_area_circulo(radio):
    """Recibe el radio y devuelve el área del círculo."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Recibe el radio y devuelve el perímetro del círculo."""
    return 2 * math.pi * radio

# Solicitar el radio al usuario
print("\n--- Ejercicio 4 ---")
# Convertimos la entrada a float (número decimal)
radio_circulo = float(input("Ingresá el radio del círculo: "))

# Llamar ambas funciones
area = calcular_area_circulo(radio_circulo)
perimetro = calcular_perimetro_circulo(radio_circulo)

# Mostramos los resultados (:.2f formatea a 2 decimales)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


def segundos_a_horas(segundos):
    """Recibe segundos y devuelve la cantidad de horas."""
    # 1 hora = 3600 segundos
    return segundos / 3600

# Solicitar segundos al usuario
print("\n--- Ejercicio 5 ---")
segundos_totales = int(input("Ingresá la cantidad de segundos: "))

horas_calculadas = segundos_a_horas(segundos_totales)

print(f"{segundos_totales} segundos equivalen a {horas_calculadas:.2f} horas.")


def tabla_multiplicar(numero):
    """
    Recibe un número e imprime su tabla de multiplicar del 1 al 10.
    """
    print(f"--- Tabla de multiplicar del {numero} ---")
    # Usamos un bucle 'for' que va desde 1 hasta 10
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Pedir al usuario el número
print("\n--- Ejercicio 6 ---")
numero_tabla = int(input("Ingresá un número para ver su tabla: "))
tabla_multiplicar(numero_tabla)

def operaciones_basicas(a, b):
    """
    Recibe dos números y devuelve una tupla con la suma,
    resta, multiplicación y división.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Buena práctica: chequear la división por cero
    if b != 0:
        division = a / b
    else:
        # Usamos None para indicar que la operación no fue posible
        division = None 
    
    # Retornamos la tupla con los resultados
    return (suma, resta, multiplicacion, division)

# Pedir números
print("\n--- Ejercicio 7 ---")
num1 = float(input("Ingresá el primer número (a): "))
num2 = float(input("Ingresá el segundo número (b): "))

# Desempaquetamos la tupla que devuelve la función
suma_res, resta_res, multi_res, divi_res = operaciones_basicas(num1, num2)

print(f"Suma: {suma_res}")
print(f"Resta: {resta_res}")
print(f"Multiplicación: {multi_res}")

if divi_res is not None:
    print(f"División: {divi_res:.2f}")
else:
    print("División: No se puede dividir por cero.")
    

def calcular_imc(peso, altura):
    """
    Recibe peso (kg) y altura (m), y devuelve el IMC.
    IMC = peso / (altura * altura)
    """
    # Chequeamos que la altura sea válida
    if altura <= 0:
        return None
    
    return peso / (altura ** 2)

# Solicitar al usuario los datos
print("\n--- Ejercicio 8 ---")
peso_kg = float(input("Ingresá tu peso en kg (ej: 70.5): "))
altura_m = float(input("Ingresá tu altura en metros (ej: 1.75): "))

imc = calcular_imc(peso_kg, altura_m)

# Mostramos el resultado con dos decimales
if imc is not None:
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
else:
    print("Error: La altura ingresada no es válida.")
    
    
def celsius_a_fahrenheit(celsius):
    """
    Recibe grados Celsius y devuelve su equivalente en Fahrenheit.
    F = (C * 9/5) + 32
    """
    return (celsius * 9/5) + 32

# Pedir al usuario la temperatura
print("\n--- Ejercicio 9 ---")
temp_celsius = float(input("Ingresá la temperatura en grados Celsius: "))

temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C equivale a {temp_fahrenheit:.2f}°F.")


def calcular_promedio(a, b, c):
    """Recibe tres números y devuelve su promedio."""
    return (a + b + c) / 3

# Solicitar los números al usuario
print("\n--- Ejercicio 10 ---")
n1 = float(input("Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))
n3 = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio de los tres números es: {promedio:.2f}")

