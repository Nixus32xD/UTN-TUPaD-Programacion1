# Ejercicio FOR 
print("=== ENCRIPTACIÓN DE MENSAJES (CIFRA DEL CÉSAR) ===")

# Alfabeto español (27 letras)
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Ingrese el corrimiento (número de lugares a correr): "))

for i in range(5):
    print(f"\n--- Mensaje {i+1} ---")
    mensaje_original = input("Ingrese el mensaje a encriptar: ").lower()
    mensaje_encriptado = ""
    
    for letra in mensaje_original:
        if letra in alfabeto:
            posicion_actual = alfabeto.index(letra)
            nueva_posicion = (posicion_actual + corrimiento) % 27
            letra_encriptada = alfabeto[nueva_posicion]
            mensaje_encriptado += letra_encriptada
        else:
            mensaje_encriptado += letra
    
    print(f"Mensaje encriptado: {mensaje_encriptado.upper()}")


# Ejercicio WHILE - Piedra, Papel o Tijeras
import random

print("\n=== PIEDRA, PAPEL O TIJERAS ===")

victorias_jugador = 0
victorias_computadora = 0
empates = 0

opciones = ["piedra", "papel", "tijera"]

while True:
    print("\n--- Menú ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    
    opcion = input("Elija una opción (1-4): ")
    
    if opcion == "4":
        break
    
    if opcion not in ["1", "2", "3"]:
        print("Opción no válida. Intente nuevamente.")
        continue
    
    elecciones = {"1": "piedra", "2": "papel", "3": "tijera"}
    jugador = elecciones[opcion]
    computadora = random.choice(opciones)
    
    print(f"\nTú elegiste: {jugador.upper()}")
    print(f"La computadora eligió: {computadora.upper()}")
    
    if jugador == computadora:
        print("¡EMPATE!")
        empates += 1
    elif (jugador == "piedra" and computadora == "tijera") or (jugador == "tijera" and computadora == "papel") or (jugador == "papel" and computadora == "piedra"):
        print("¡GANASTE!")
        victorias_jugador += 1
    else:
        print("¡La computadora GANA!")
        victorias_computadora += 1
    
    print(f"\nMarcador: Tú {victorias_jugador} - {victorias_computadora} Computadora (Empates: {empates})")

print("\n=== RESULTADO FINAL ===")
print(f"Partidas ganadas por ti: {victorias_jugador}")
print(f"Partidas ganadas por la computadora: {victorias_computadora}")
print(f"Empates: {empates}")
print("¡Gracias por jugar!")