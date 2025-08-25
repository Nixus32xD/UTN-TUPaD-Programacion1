# 1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección. 
numero1 = 15
print(f"1. numero1 = {numero1}")

print("----------------------------------------------------------------------------------")
# 2. No borres la variable número uno y crea una variable llamada "numero2" asignándole 
# un número decimal de tu elección. 
numero2 = 7.5
print(f"2. numero2 = {numero2}")

print("----------------------------------------------------------------------------------")
# 3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2". 
suma = numero1 + numero2
print(f"3. suma = {numero1} + {numero2} = {suma}")

print("----------------------------------------------------------------------------------")
# 4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para 
# multiplicación y otra para división. Imprime estas variables. 
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"4. Operaciones matemáticas:")
print(f"   Resta: {numero1} - {numero2} = {resta}")
print(f"   Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"   División: {numero1} / {numero2} = {division}")

print("----------------------------------------------------------------------------------")
# 5. Crea una variable llamada "nombre" y asígnale tu nombre como valor. 
nombre = "Nicolas"
print(f"5. Nombre: '{nombre}'")

print("----------------------------------------------------------------------------------")
# 6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el 
# precio de un artículo ficticio. 
precio = 89.68
print(f"6. precio = ${precio}")

print("----------------------------------------------------------------------------------")
# 7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale 
# un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le 
# quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 
# 100% y el valor 0 al 0%. 
descuento = 0.25
print(f"7. descuento = {descuento * 100}%")

print("----------------------------------------------------------------------------------")
# 8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y 
# almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que 
# aplica la lógica de matemáticas. 
precio_final = precio * (1 - descuento)
print(f"8. precio_final = ${precio_final}")

print("----------------------------------------------------------------------------------")
# 9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu 
# elección. Qué sea un string. 
cadena = "Me gusta mucho lo q es la programación"
print(f"9. cadena: '{cadena}'")

print("----------------------------------------------------------------------------------")
# 10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas 
# a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de 
# Python. 
longitud = len(cadena)
print(f"10. longitud: {longitud} caracteres")

print("----------------------------------------------------------------------------------")
# 11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y 
# conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo 
# mismo. 
precio_decimal = 45.67
precio_entero = int(precio_decimal)
print(f"11. precio_decimal = {precio_decimal}")

print("----------------------------------------------------------------------------------")
# 12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas 
# en una tercera variable llamada "nombre_completo", el nombre y el apellido con un 
# espacio entre medio. Puedes usar libremente la forma de concatenación que quieras. 
nombre_persona = "Nicolas"
apellido = "Moron"
nombre_completo = nombre_persona + " " + apellido
print(f"12. nombre_completo: {nombre_completo}")

print("----------------------------------------------------------------------------------")
# 13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10. 
edad = 25
print(f"13. edad inicial = {edad}")
edad += 5
print(f"    edad después de incrementar 5 = {edad}")
edad -= 10
print(f"    edad después de disminuir 10 = {edad}")

print("----------------------------------------------------------------------------------")
# 14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y 
# centímetros. Por ejemplo: 1.83.  Multiplícala por 4 y luego divídela en 3. 
altura = 1.75
print(f"14. altura inicial = {altura}m")
altura_multiplicada = altura * 4
print(f"    altura × 4 = {altura_multiplicada}m")
altura_dividida = altura_multiplicada / 3
print(f"    altura / 3 = {altura_dividida}m")

print("----------------------------------------------------------------------------------")
# 15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después 
# transfórmalo todo en minúsculas con algún método o función de Python. 
nombre_mayusculas = "NICOLAS"
nombre_minusculas = nombre_mayusculas.lower()
print(f"15. nombre_mayusculas = '{nombre_mayusculas}'")
print(f"    nombre_minusculas = '{nombre_minusculas}'")

print("----------------------------------------------------------------------------------")
# 16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido 
# para que se transforme todo en minúsculas excepto la primera letra. 
nombre_capitalizado = nombre_mayusculas.capitalize()
print(f"16. nombre_capitalizado = '{nombre_capitalizado}'")

print("----------------------------------------------------------------------------------")
# Mostrar todas las variables al final
print("RESUMEN DE TODAS LAS VARIABLES:")
print(f"numero1 = {numero1}")
print(f"numero2 = {numero2}")
print(f"suma = {suma}")
print(f"resta = {resta}")
print(f"multiplicacion = {multiplicacion}")
print(f"division = {division}")
print(f"nombre = '{nombre}'")
print(f"precio = {precio}")
print(f"descuento = {descuento}")
print(f"precio_final = {precio_final:.2f}")
print(f"cadena = '{cadena}'")
print(f"longitud = {longitud}")
print(f"precio_decimal = {precio_decimal}")
print(f"precio_entero = {precio_entero}")
print(f"nombre_persona = '{nombre_persona}'")
print(f"apellido = '{apellido}'")
print(f"nombre_completo = '{nombre_completo}'")
print(f"edad = {edad}")
print(f"altura = {altura}")
print(f"altura_multiplicada = {altura_multiplicada}")
print(f"altura_dividida = {altura_dividida:.2f}")
print(f"nombre_mayusculas = '{nombre_mayusculas}'")
print(f"nombre_minusculas = '{nombre_minusculas}'")
print(f"nombre_capitalizado = '{nombre_capitalizado}'")