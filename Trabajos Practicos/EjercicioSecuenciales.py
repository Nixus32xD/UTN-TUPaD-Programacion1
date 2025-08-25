# Calculadora de propinas en un restaurante 
# Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el 
# monto de la cuenta. 

print("----------------------------------------------------------------------------------")
print("CALCULADORA DE PROPINAS")
print("----------------------------------------------------------------------------------")

# Pedir al usuario el monto total de la cuenta.
monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

# Calcular la propina sugerida al 10%.
propina_10 = monto_cuenta * 0.10

# Calcular la propina sugerida al 15%.
propina_15 = monto_cuenta * 0.15

# Calcular el total a pagar en ambos casos (cuenta + propina).
total_propina_10 = monto_cuenta + propina_10
total_propina_15 = monto_cuenta + propina_15

# Mostrar todos los resultados en pantalla.
print("----------------------------------------------------------------------------------")
print("RESULTADOS:")
print("----------------------------------------------------------------------------------")
print(f"Propina sugerida (10%): {propina_10}")
print(f"Total a pagar (10%): {total_propina_10}")
print(f"Propina sugerida (15%): {propina_15}")
print(f"Total a pagar (15%): {total_propina_15}")
print("----------------------------------------------------------------------------------")