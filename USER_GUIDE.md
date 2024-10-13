# Guía de Usuario 

## 1. Instrucciones de Instalación y Ejecución:

Antes de empezar, debes tener lo siguiente instalado en tu computadora: (Python 3.12)

### Clonación del repositorio

1. Abrir una terminal (Git bash).

2. Clonar el repositorio usando el siguiente codigo:

    git clone 'URL' del repositorio.

3. Navegar en el directorio del proyecto:

    cd "nombre_proyecto"

4. Ejecutar el programa:

Para ejecutar el programa se debe abrir "visual studio code" luego se entra a la terminal y se comprueba si el código funciona o no. 

## 2. Uso del Programa

### Menú principal

Este programa presenta un menú que permite al usuario realizar distintas acciones relacionadas con la gestión de productos en un inventario.

Opciones del menú:

    1. Agregar producto: Permite agregar un nuevo producto al inventario.
    2. Modificar producto: Permite modificar la información de un producto existente en el inventario.
    3. Eliminar producto: Elimina un producto del inventario.
    4. Consultar Inventario: Muestra todos los productos del inventario.
    5. Buscar producto: Busca un producto específico por su código.
    0. Salir: Finaliza el programa.

### Instrucciones de uso

Al iniciar el programa, se mostrará un menú donde el usuario puede seleccionar la opción que desea realizar. A continuación se detalla cada opción:

    1. Agregar producto: Al seleccionar esta opción, el programa solicitará el nombre, código, cantidad y precio del nuevo producto para agregarlo al inventario.
    2. Modificar producto: El usuario debe ingresar el código del producto que desea modificar. Si el producto existe, se podrán cambiar su nombre, cantidad y precio.
    3. Eliminar producto: El usuario debe ingresar el código del producto que desea eliminar. Si el producto existe, será eliminado del inventario.
    4. Consultar Inventario: Muestra todos los productos en el inventario con su respectiva información.
    5. Buscar producto: Permite buscar un producto específico por su código. Si el producto se encuentra, se muestra su información.

### Comandos

El programa responde a las siguientes opciones en el menú:

    1: Agregar un nuevo producto.
    2: Modificar un producto existente.
    3: Eliminar un producto.
    4: Consultar el inventario completo.
    5: Buscar un producto por su código.
    0: salir del programa.

## 3. Ejemplos

A continuación, se presentan algunos ejemplos sobre el uso del programa:

### Ejemplo 1: Agregar un producto

    1. Seleccionar la opción "1" en el menú.
    2. Ingresar la información solicitada:
        Nombre del producto: Gaseosa
        Código del producto: 001
        Cantidad: 20
        Precio: 3.500
    3. El programa añadirá el producto al inventario y mostrará el siguente mensaje:
        "Producto agregado correctamente al inventario."

### Ejemplo 2: Modificar un producto

    1. Seleccionar la opción "2" en el menú.
    2. Ingresar el código del producto a modificar: 001.
    3. Cambiar la información del producto:
        Nuevo nombre: Gaseosa grande
        Nueva cantidad: 30
        Nuevo precio: 8.000
    4. El programa actualizará el producto en el inventario.

### Ejemplo 3: Eliminar un producto

    1. Seleccionar la opción "3" en el menú.
    2. Ingresar el código del producto a eliminar: 001.
    3. El programa eliminará el producto del inventario y mostrará el mensaje:
        Producto eliminado: {'nombre': 'Gaseosa grande', 'codigo': '001', 'cantidad': 30, 'precio': 8.000}

### Ejemplo 4: Consultar el inventario

    1. Seleccionar la opción "4" en el menú.
    2. El programa mostrará todos los productos en el inventario en formato de diccionario, por ejemplo:
        {'001': {'nombre': 'Gaseosa', 'codigo': '001', 'cantidad': 20, 'precio': 3.500}}

### Ejemplo 5: Buscar un producto

    1. Seleccionar la opción "5" en el menú.
    2. Ingresar el código del producto: 001.
    3. El programa mostrará la información del producto:
        {'nombre': 'Gaseosa', 'codigo': '001', 'cantidad': 20, 'precio': 3.500}

### Salida

Para salir del programa, seleccionar la opción "0" en el menú.