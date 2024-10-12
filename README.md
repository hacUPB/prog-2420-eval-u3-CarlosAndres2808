[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: Carlos Andrés Vásquez Vargas
ID: 000540434
---
 
#### Título del Proyecto:

Sistema de Inventario para una Tienda

#### Descripción Detallada:

El proyecto consiste en desarrollar un sistema de inventario para una tienda, en este sistema el usuario podrá agregar, actualizar, eliminar y consultar productos disponibles en la tienda. Cada producto tiene un nombre, cantidad disponible y precio. Este sistema sirve para pequeños negocios que requieren gestionar su inventario de manera eficiente y evitar desabastecimientos o el exceso de productos.

#### Alcance:

•   Funcionalidades principales:

	•   Agregar nuevos productos al inventario.

	•   Eliminar productos existentes del inventario.

	•	Actualizar información de un producto, como la cantidad y el precio.

	•	Consultar el inventario para ver los productos disponibles.

	•	Buscar un producto específico por su nombre.

•   Casos que cubrirá:

	•	Gestionar el inventario cuando está creciendo.

	•	Mantener la información actualizada de cada producto.

	•	Evitar errores de inventario (productos duplicados, falta de información, etc.)

#### Estructuras de Datos Utilizadas:

	•	Diccionario: Se usará para almacenar los productos, con el nombre del producto como clave, y sus detalles (cantidad y precio) como valores específicos. 

#### Pseudocódigo: 

Inicio

    Mostrar Menú Principal

    Repetir hasta que el usuario elija la opción 6:

        1. Agregar Producto

            Solicitar nombre, cantidad, precio del producto
            Guardar el producto en el diccionario

        2. Eliminar Producto

            Solicitar nombre del producto
            Si el producto existe en el diccionario: 
                Eliminar el producto del diccionario
            Si no:
                Mostrar mensaje "Producto no encontrado"

        3. Actualizar Producto

            Solicitar nombre del producto
            Si el producto existe en el diccionario:
                Solicitar si desea actualizar cantidad o precio
                Actualizar la información correspondiente
            Si no:
                Mostrar mensaje "Producto no encontrado"
        4. Consultar Inventario

            Mostrar todos los productos y su información (nombre, cantidad, precio)

        5. Buscar Producto

            Solicitar nombre del producto
            Si el producto existe en el diccionario:
                Mostrar detalles del producto
            Si no:
                Mostrar mensaje "Producto no encontrado"

        6. Salir

            Finalizar el programa

Fin


