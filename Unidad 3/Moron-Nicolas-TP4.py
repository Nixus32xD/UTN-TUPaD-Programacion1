# Ejercicio 1
print("Ejercicio 1:")
for i in range(101):
    print(i)

# Ejercicio 2
print("\nEjercicio 2:")
numero = input("Ingrese un número: ")
print("Tiene", len(numero), "dígitos")

# Ejercicio 3
print("\nEjercicio 3:")
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
suma = 0
for i in range(min(a,b)+1, max(a,b)):
    suma += i
print("Suma:", suma)

# Ejercicio 4
print("\nEjercicio 4:")
total = 0
while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Total:", total)

# Ejercicio 5
print("\nEjercicio 5:")
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina (0-9): "))
    intentos += 1
    if intento == secreto:
        break
print("Adivinaste en", intentos, "intentos")

# Ejercicio
print("\nEjercicio 6:")
for i in range(100, -1, -2):
    print(i)

# Ejer
print("\nEjercicio 7:")
n = int(input("Ingrese n: "))
suma = 0
for i in range(n+1):
    suma += i
print("Suma:", suma)

# Ejercicio 8:
print("\nEjercicio 8:")
pares = impares = positivos = negativos = 0
for i in range(100):  # Cambiar por un número menor para pruebas rápidas
    num = int(input("Número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9:
print("\nEjercicio 9:")
suma = 0
for i in range(100):                # Aca tambien cambiar el 100 por un numero menor
    num = int(input("Número: "))
    suma += num
print("Media:", suma/100)           # Y aca tambien 

# Ejercicio 10
print("\nEjercicio 10:")
numero = input("Ingrese número: ")
print("Invertido:", numero[::-1])