# -----------------------------------------------------------------
# UTN - Tecnicatura Universitaria en Programación
# Práctico 6: Estructuras de datos complejas
# Resolución completa en un único archivo
# -----------------------------------------------------------------

# --- Ejercicios 1, 2 y 3: Precios de Frutas ---
# (Estos tres ejercicios se encadenan)

print("--- Ejercicios 1, 2 y 3: Precios de Frutas ---")

# 1. Definir diccionario y añadir frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario original: {precios_frutas}")

# Añadimos las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(f"Diccionario (1) + agregados: {precios_frutas}")

# 2. Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(f"Diccionario (2) + actualizados: {precios_frutas}")

# 3. Lista de frutas (solo las claves)
# Convertimos la vista de .keys() en una lista
lista_de_frutas = list(precios_frutas.keys())
print(f"Lista de frutas (3): {lista_de_frutas}")


# --- Ejercicio 4: Agenda Telefónica ---
print("\n--- Ejercicio 4: Agenda Telefónica ---")

contactos = {}

# [cite_start]Permitir al usuario cargar 5 contactos [cite: 71]
print("Por favor, cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    numero = input(f"Número de {nombre}: ")
    contactos[nombre] = numero

print(f"\nAgenda cargada: {contactos}")

# [cite_start]Pedir un nombre y mostrar el número asociado [cite: 72]
nombre_consulta = input("\nIngresá un nombre para buscar su número: ")

# Usamos .get() para manejar el caso de que el contacto no exista
numero_encontrado = contactos.get(nombre_consulta, "Contacto no encontrado.")
print(f"Resultado de la búsqueda: {numero_encontrado}")


# --- Ejercicio 5: Análisis de Frase ---
print("\n--- Ejercicio 5: Análisis de Frase ---")

# [cite_start]Solicitar al usuario una frase [cite: 80]
frase = input("Ingresá una frase: ")

# Preparamos la lista de palabras (en minúsculas y separadas)
palabras = frase.lower().split()

# [cite_start]1. Palabras únicas (usando un set) [cite: 81]
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# [cite_start]2. Diccionario con la cantidad de veces que aparece cada palabra [cite: 82]
recuento_palabras = {}
for palabra in palabras:
    # Usamos .get() para obtener el conteo actual (o 0 si es la primera vez)
    # y le sumamos 1
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

print(f"Recuento de palabras: {recuento_palabras}")


# --- Ejercicio 6: Promedio de Alumnos ---
print("\n--- Ejercicio 6: Promedio de Alumnos ---")

alumnos = {} # El diccionario almacenará: "Nombre": (nota1, nota2, nota3)

# [cite_start]Permitir ingresar los nombres de 3 alumnos y sus notas [cite: 88]
print("Ingresá los datos de 3 alumnos:")
for _ in range(3):
    nombre_alumno = input("Nombre del alumno: ")
    
    # Pedimos las 3 notas
    n1 = float(input(f"Nota 1 de {nombre_alumno}: "))
    n2 = float(input(f"Nota 2 de {nombre_alumno}: "))
    n3 = float(input(f"Nota 3 de {nombre_alumno}: "))
    
    # [cite_start]Guardamos las notas como una tupla [cite: 88]
    notas_tupla = (n1, n2, n3)
    alumnos[nombre_alumno] = notas_tupla

print("\n--- Promedios de Alumnos ---")
# [cite_start]Mostrar el promedio de cada alumno [cite: 89]
for alumno, notas in alumnos.items():
    # Sumamos los elementos de la tupla y dividimos por la cantidad (3)
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")


# --- Ejercicio 7: Operaciones de Sets (Parciales) ---
print("\n--- Ejercicio 7: Operaciones de Sets (Parciales) ---")

# [cite_start]Datos de ejemplo (el TP no los provee, así que los definimos) [cite: 97]
parcial_1_aprobados = {"Ana", "Luis", "Sofía", "Juan", "Marta", "Diego"}
parcial_2_aprobados = {"Luis", "Marta", "Pedro", "Elena", "Sofía", "Ana"}

print(f"Aprobaron P1: {parcial_1_aprobados}")
print(f"Aprobaron P2: {parcial_2_aprobados}")

# [cite_start]1. Mostrar los que aprobaron ambos parciales (Intersección) [cite: 98]
ambos_parciales = parcial_1_aprobados.intersection(parcial_2_aprobados)
# Alternativa: ambos_parciales = parcial_1_aprobados & parcial_2_aprobados
print(f"\nAprobaron ambos parciales: {ambos_parciales}")

# [cite_start]2. Mostrar los que aprobaron solo uno de los dos (Diferencia simétrica) [cite: 99]
solo_un_parcial = parcial_1_aprobados.symmetric_difference(parcial_2_aprobados)
# Alternativa: solo_un_parcial = parcial_1_aprobados ^ parcial_2_aprobados
print(f"Aprobaron solo uno de los dos parciales: {solo_un_parcial}")

# [cite_start]3. Mostrar la lista total de estudiantes (Unión) [cite: 100]
total_aprobados = parcial_1_aprobados.union(parcial_2_aprobados)
# Alternativa: total_aprobados = parcial_1_aprobados | parcial_2_aprobados
print(f"Total de alumnos que aprobaron al menos un parcial: {total_aprobados}")


# --- Ejercicio 8: Gestión de Stock ---
print("\n--- Ejercicio 8: Gestión de Stock ---")

# [cite_start]Diccionario inicial de stock [cite: 101]
stock = {"Teclado": 50, "Mouse": 70, "Monitor": 30}
print(f"Stock inicial: {stock}")

# [cite_start]1. Consultar el stock de un producto ingresado [cite: 102]
producto_consulta = input("Ingresá un producto para consultar stock (ej: Mouse): ")
stock_disponible = stock.get(producto_consulta, "Producto no encontrado")
print(f"Stock de {producto_consulta}: {stock_disponible}")

# 2. Lógica para agregar productos o stock
producto_agregar = input("\nIngresá el producto a agregar/actualizar (ej: Teclado o Silla): ")
cantidad_agregar = int(input(f"Cantidad a agregar de {producto_agregar}: "))

if producto_agregar in stock:
    # [cite_start]3. Agregar unidades al stock si el producto ya existe [cite: 103]
    stock[producto_agregar] += cantidad_agregar
    print(f"Stock de {producto_agregar} actualizado.")
else:
    # [cite_start]4. Agregar un nuevo producto si no existe [cite: 104]
    stock[producto_agregar] = cantidad_agregar
    print(f"Se agregó el nuevo producto {producto_agregar} al stock.")

print(f"Stock final: {stock}")


# --- Ejercicio 9: Agenda (Tupla como Key) ---
print("\n--- Ejercicio 9: Agenda (Tupla como Key) ---")

# [cite_start]Agenda donde las claves son tuplas (día, hora) [cite: 105, 112, 113]
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "09:00"): "Desayuno con cliente",
    ("lunes", "14:30"): "Entrevista"
}
print("Agenda cargada.")

# [cite_start]Permitir consultar qué actividad hay en cierto día y hora [cite: 117]
print("Consultar agenda:")
dia_consulta = input("Ingresá el día (ej: lunes): ").lower()
hora_consulta = input("Ingresá la hora (ej: 10:00): ")

# Creamos la tupla para la consulta
consulta = (dia_consulta, hora_consulta)

# Consultamos el evento usando .get()
evento = agenda.get(consulta, "No hay eventos programados en esa fecha y hora.")
print(f"Evento: {evento}")


# --- Ejercicio 10: Invertir Diccionario ---
print("\n--- Ejercicio 10: Invertir Diccionario ---")

# [cite_start]Diccionario que mapea países con capitales [cite: 118, 122]
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

print(f"Diccionario original: {paises_capitales}")

# [cite_start]Construir el nuevo diccionario invertido [cite: 119, 120]
capitales_paises = {}

# Iteramos sobre los pares (clave, valor) del original
for pais, capital in paises_capitales.items():
    # En el nuevo, la capital es la clave y el país es el valor
    capitales_paises[capital] = pais

print(f"Diccionario invertido: {capitales_paises}")