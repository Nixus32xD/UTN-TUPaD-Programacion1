# ===================  Actividad 1  ===================

def crear_archivo_inicial():
    """Crea el archivo con tres productos iniciales"""
    productos_iniciales = [
        "Computadora,1000000.0,6",
        "Mouse,5000.0,15",
        "Cuaderno,100.0,25"
    ]
    
    with open("productos.txt", "w") as archivo:
        for producto in productos_iniciales:
            archivo.write(producto + "\n")
    print("Archivo creado con productos iniciales")

# ===================  Actividad 2  ===================

def leer_y_mostrar_productos():
    """Lee el archivo y muestra los productos"""
    try:
        with open("productos.txt", "r") as archivo:
            print("===== LISTA DE PRODUCTOS =====")
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    nombre, precio, cantidad = datos
                    print(f"Producto: {nombre} - Precio: ${precio} - Cantidad: {cantidad}")
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'productos.txt'")

# ===================  Actividad 3  ===================

def agregar_producto():
    """Permite al usuario agregar un nuevo producto al archivo"""
    print("===== AGREGAR NUEVO PRODUCTO =====")
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio")
    
    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad")
    
    # Agregar al archivo
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"Producto '{nombre}' agregado exitosamente!")

# ===================  Actividad 4  ===================

def cargar_productos():
    """Carga los productos del archivo en una lista de diccionarios"""
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    producto = {
                        "nombre": datos[0],
                        "precio": float(datos[1]),
                        "cantidad": int(datos[2])
                    }
                    productos.append(producto)
        print(productos)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'productos.txt'")
    except ValueError as e:
        print(f"Error en el formato de datos: {e}")
    
    return productos

# ===================  Actividad 5  ===================

def buscar_producto(productos):
    """Busca un producto por nombre en la lista de productos"""
    if not productos:
        print("No hay productos cargados para buscar")
        return
    
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"PRODUCTO ENCONTRADO:")
            print(f"   Nombre: {producto['nombre']}")
            print(f"   Precio: ${producto['precio']}")
            print(f"   Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Producto '{nombre_buscar}' no encontrado")

# ===================  Actividad 6  ===================

def guardar_productos(productos):
    """Guarda la lista de productos actualizada en el archivo"""
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        print("Archivo actualizado exitosamente!")
    except Exception as e:
        print(f"Error al guardar el archivo")


# Función principal que integra todas las actividades
def main():
    """Función principal que ejecuta el programa completo"""
    print("=" * 50)
    print("      SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("=" * 50)
    
    # Crear archivo inicial si no existe
    try:
        with open("productos.txt", "r"):
            pass
    except FileNotFoundError:
        crear_archivo_inicial()
    
    productos = []
    
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Mostrar todos los productos")
        print("2. Agregar nuevo producto")
        print("3. Recargar productos desde archivo")
        print("4. Buscar producto por nombre")
        print("5. Guardar productos en archivo")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            leer_y_mostrar_productos()
        
        elif opcion == "2":
            agregar_producto()
            # Actualizar la lista en memoria
            productos = cargar_productos()
        
        elif opcion == "3":
            if not productos:
                productos = cargar_productos()
            buscar_producto(productos)
        
        elif opcion == "4":
            productos = cargar_productos()
        
        elif opcion == "5":
            if not productos:
                productos = cargar_productos()
            guardar_productos(productos)
        
        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione 1-6")

main()