# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

print("----------------------------------------------------------------------------------")
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla. 
print("----------------------------------------------------------------------------------")
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
lugar_residencia = input("Por favor, ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 
print("----------------------------------------------------------------------------------")
import math

radio = float(input("Por favor, ingrese el radio del circulo: "))
area = math.pi * (radio ** 2)
primetro = 2 * math.pi * radio
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {primetro}")

print("----------------------------------------------------------------------------------")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.

segundos = int(input("Por favor, ingrese una cantidad en segundos:"))
print(f"{segundos} segundos equivalen a {segundos /3600} horas")

print("----------------------------------------------------------------------------------")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

numero = int(input("Por favor, ingrese un numero:"))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
    
print("----------------------------------------------------------------------------------")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

numero1 = int(input("Por favor, ingrese el primer numero (distinto de 0): "))
numero2 = int(input("Por favor, ingrese el segundo numero (distinto de 0): "))
if numero1 == 0 or numero2 == 0:
    print("Los numeros deben ser distintos de 0.")
else:
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    if numero2 != 0:
        division = numero1 / numero2
    else:
        division = "Indefinido (no se puede dividir por cero)"
    
    print(f"Suma: {numero1} + {numero2} = {suma}")
    print(f"Resta: {numero1} - {numero2} = {resta}")
    print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
    print(f"División: {numero1} / {numero2} = {division}")

print("----------------------------------------------------------------------------------")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal.}

altura = float(input("Por favor, ingrese su altura en metros: "))
peso = float(input("Por favor, ingrese su peso en kilogramos: "))

if altura > 0 and peso > 0:
    imc = peso / (altura ** 2)
    print(f"Su indice de masca corportal (IMC) es: {imc}")
else:
    print("La altura y el peso deben ser mayores a 0.")


print("----------------------------------------------------------------------------------")

#  9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Por favor, ingrese una temperatura en grados Celsius:"))
fahrenheit = (9/5 * celsius) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

print("----------------------------------------------------------------------------------")

#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números.

numero1 = float(input("Por favor, ingrese el primer numero: "))
numero2 = float(input("Por favor, ingrese el segundo numero: "))
numero3 = float(input("Por favor, ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los numeros {numero1}, {numero2} y {numero3} es: {promedio}")

print("----------------------------------------------------------------------------------")