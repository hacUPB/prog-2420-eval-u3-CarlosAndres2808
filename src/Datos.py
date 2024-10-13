# Función para agregar un producto al inventario
def agregar_producto(inventario):
    # Solicitar información al usuario sobre el producto
    nombre = input("Nombre del producto: ")
    codigo = input("Código del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    # Diccionario para agregar el nuevo producto    
    nuevo_producto = {
        "nombre": nombre,
        "codigo": codigo, 
        "cantidad": cantidad, 
        "precio": precio
    }
    # Agregar un producto al inventario utilizando el código como clave
    inventario[codigo] = nuevo_producto
    print("Producto agregado correctamente.")
# Función para modificar un producto
def modificar_producto(inventario, codigo):
    producto = buscar_producto(inventario, codigo)

    # Si el producto no existe
    if producto is None:
        return
    
    # Modificar campos del producto
    producto["nombre"] = input("Nuevo nombre: ")
    producto["cantidad"] = int(input("Nueva cantidad: "))
    producto["precio"] = float(input("Nuevo precio: "))

    # Actualizar producto en el inventario
    inventario[codigo] = producto
# Función para eliminar un producto del inventario
def eliminar_producto(inventario, codigo):
    producto = buscar_producto(inventario, codigo)

    # Si el producto no existe
    if producto is None:
        return

    del inventario[codigo]
    print("Producto eliminado: ", producto)
# Función para consultar un producto del inventario
def consultar_inventario(inventario):
    print(inventario)
# Función para buscar un producto del inventario
def buscar_producto(inventario, codigo):
    producto = inventario.get(codigo, None)
    if producto is not None:
        print(producto)
    else:
        print(f"El producto con el código {codigo} no existe")
    return producto

# Función principal que gestiona el menú y las operaciones del inventario
def main():

    # Inicializamos el inventario
    inventario = {}

    while True:
        # Menú principal
        print("Menú:")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Consultar Inventario")
        print("5. Buscar producto")
        print("0. Salir")
        
        # Solicita al usuario que seleccione una opción
        opcion = input("Selecciona una opción: ")
        # Dependiendo de la opción seleccionada, se llama a la función correspondiente
        if opcion == "1":
            agregar_producto(inventario)
        if opcion == "2":
            codigo = input("Código del producto a modificar: ")
            modificar_producto(inventario, codigo)
        if opcion == "3":
            codigo = input("Código del producto a eliminar: ")
            eliminar_producto(inventario, codigo)
        if opcion == "4":
            consultar_inventario(inventario)
        elif opcion == "5":
            codigo = input("Ingrese el código del producto: ")
            buscar_producto(inventario, codigo)
        # Si elige 0, se termina el ciclo y el programa finaliza    
        elif opcion == "0":
            break

if __name__ == "__main__":
    main()
