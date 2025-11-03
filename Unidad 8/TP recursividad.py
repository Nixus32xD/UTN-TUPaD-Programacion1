import sys
# TP: Ejercicios de Recursividad
sys.setrecursionlimit(2000)

# --- Ejercicio 1: Factorial ---
#
def factorial(n):
    """
    Calcula el factorial de un número n de forma recursiva.
    """
    # Caso Base: El factorial de 0 o 1 es 1.
    if n == 0 or n == 1:
        return 1
    # Paso Recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

def mostrar_factoriales(num):
    """
    Función auxiliar para mostrar los factoriales desde 1 hasta num.
    """
    print(f"\n--- Factoriales hasta {num} ---")
    for i in range(1, num + 1):
        print(f"Factorial de {i} = {factorial(i)}")

# --- Ejercicio 2: Fibonacci ---
#
def fibonacci(pos):
    """
    Calcula el valor de la serie de Fibonacci en la posición 'pos'
    de forma recursiva.
    """
    # Caso Base 1: F(0) = 0
    if pos == 0:
        return 0
    # Caso Base 2: F(1) = 1
    elif pos == 1:
        return 1
    # Paso Recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_serie_fibonacci(pos):
    """
    Función auxiliar para mostrar la serie completa hasta la posición.
    """
    print(f"\n--- Serie de Fibonacci hasta la posición {pos} ---")
    for i in range(pos + 1):
        print(fibonacci(i), end=" ")
    print() # Salto de línea al final

# --- Ejercicio 3: Potencia ---
#
def potencia(base, exponente):
    """
    Calcula la potencia de 'base' elevado a 'exponente'
    de forma recursiva.
    """
    # Caso Base: n^0 = 1
    if exponente == 0:
        return 1
    # Paso Recursivo: n^m = n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)

# --- Ejercicio 4: Decimal a Binario ---
#
def decimal_a_binario(n):
    """
    Convierte un número decimal 'n' a binario (string)
    de forma recursiva.
    """
    # Caso Base: Cuando el cociente es 0, no hay más que dividir.
    if n == 0:
        return ""
    # Paso Recursivo:
    # 1. Obtenemos el resto (n % 2)
    # 2. Llamamos recursivamente con el cociente (n // 2)
    # 3. Concatenamos el resultado de la recursión + el resto
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# --- Ejercicio 5: Palíndromo ---
#
def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo de forma recursiva.
    Restricciones: Sin [::-1] ni reversed()
    """
    # Caso Base 1: Si la palabra tiene 0 o 1 letra, es palíndromo.
    if len(palabra) <= 1:
        return True
    # Caso Base 2: Si la primera y última letra son distintas, no lo es.
    if palabra[0] != palabra[-1]:
        return False
    # Paso Recursivo:
    # Llamamos a la función con la palabra "recortada" (sin la primera
    # y sin la última letra).
    return es_palindromo(palabra[1:-1])

# --- Ejercicio 6: Suma de Dígitos ---
#
def suma_digitos(n):
    """
    Suma los dígitos de un número entero positivo 'n'
    de forma recursiva.
    Restricciones: Sin convertir a string.
    """
    # Caso Base: Si n es 0, no hay más dígitos que sumar.
    if n == 0:
        return 0
    # Paso Recursivo:
    # 1. Obtenemos el último dígito (n % 10)
    # 2. Sumamos el último dígito + la suma de los dígitos restantes (n // 10)
    else:
        return (n % 10) + suma_digitos(n // 10)

# --- Ejercicio 7: Pirámide de Bloques ---
#
def contar_bloques(n):
    """
    Calcula el total de bloques en una pirámide donde la base tiene 'n'
    bloques y cada nivel superior tiene uno menos.
    """
    # Caso Base: Si n=1 (último nivel), solo hay 1 bloque.
    if n == 1:
        return 1
    # Paso Recursivo: n + (n-1) + (n-2) ... + 1
    else:
        return n + contar_bloques(n - 1)

# --- Ejercicio 8: Contar Dígito ---
#
def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un 'digito' en 'numero'
    de forma recursiva.
    """
    # Caso Base: Si el número es 0, no quedan dígitos por revisar.
    if numero == 0:
        return 0

    # Variable para contar si el último dígito coincide
    conteo = 0
    
    # Verificamos si el último dígito es el que buscamos
    if numero % 10 == digito:
        conteo = 1
    
    # Paso Recursivo:
    # Retornamos el conteo (0 o 1) + el resultado de buscar
    # en el resto del número (numero // 10)
    return conteo + contar_digito(numero // 10, digito)


# --- Bloque Principal para Probar las Funciones ---
if __name__ == "__main__":
    
    print("========= TP RECURSIVIDAD - PRUEBAS =========")

    # Prueba Ejercicio 1
    mostrar_factoriales(5)

    # Prueba Ejercicio 2
    mostrar_serie_fibonacci(10)

    # Prueba Ejercicio 3
    print("\n\n--- Prueba de Potencia ---")
    print(f"Potencia de 2^5 = {potencia(2, 5)}")
    print(f"Potencia de 10^3 = {potencia(10, 3)}")
    
    # Prueba Ejercicio 4
    print("\n--- Prueba Decimal a Binario ---")
    print(f"El número 10 en binario es: {decimal_a_binario(10)}")
    print(f"El número 25 en binario es: {decimal_a_binario(25)}")

    # Prueba Ejercicio 5
    print("\n--- Prueba Palíndromo ---")
    print(f"¿'neuquen' es palíndromo? {es_palindromo('neuquen')}")
    print(f"¿'radar' es palíndromo? {es_palindromo('radar')}")
    print(f"¿'python' es palíndromo? {es_palindromo('python')}")

    # Prueba Ejercicio 6
    print("\n--- Prueba Suma de Dígitos ---")
    print(f"Suma de dígitos de 1234 = {suma_digitos(1234)}")
    print(f"Suma de dígitos de 305 = {suma_digitos(305)}")
    
    # Prueba Ejercicio 7
    print("\n--- Prueba Pirámide de Bloques ---")
    print(f"Bloques para n=4: {contar_bloques(4)}")
    print(f"Bloques para n=5: {contar_bloques(5)}")

    # Prueba Ejercicio 8
    print("\n--- Prueba Contar Dígito ---")
    print(f"Veces que aparece el 2 en 12233421: {contar_digito(12233421, 2)}")
    print(f"Veces que aparece el 5 en 5555: {contar_digito(5555, 5)}")
    print(f"Veces que aparece el 7 en 123456: {contar_digito(123456, 7)}")
    
    print("\n=============================================")