# Ejercicios Prueba Técnica para Desarrollador Junior RPA

El presente repositorio contiene las soluciones para los ejercicios asignados en la prueba técnica para el cargo de Desarrollador RPA Junior en Globaltek Development S.A. Los ejercicios fueron desarrollados con el lenguaje Python. Para cada ejercicio se presenta un script de Python (archivo .py) y un notebook de Jupyter (archivo .ipybn), y se desarrollaron de forma que no necesitan dependencias externas para ejecutarse, es decir, no es necesaria ninguna librería ni dependencia, excepto Jupyter Notebook para los archivos .ipybn. A continuación, se presentan los enunciados de cada ejercicio:

## Ejercicio 1.
Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término. Ejemplos:
Entrada : numero=3, terminos=5
Salida : 37035 #(3 + 33 + 333 + 3333 + 33333)
Entrada : numero=5, terminos=3
Salida : 615 #(5 + 55 + 555)

## Ejercicio 2.
Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las
siguientes condiciones:
1. El número debe ser divisible por cinco.
2. Si el número es mayor que 600, no se incluye en la salida.
3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.
Ejemplos:
Entrada : [24, 150, 300, 660, 295, 1050, 50]
Salida : [150, 300, 295]
Entrada : [110, 720, 307, 555, 1095, 12, 300, 1000]
Salida : [110, 555]

## Ejercicio 3.
Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz
de salida (no importa el orden). Ejemplos:
Entrada : list = [12, 25, 1, 1, 7, 25]
Salida : [[12], [7], [25, 25], [1, 1]]
Entrada : list = [6, 7, 8, 9]
Salida : [[6], [7], [8], [9]]

## Ejercicio 4.
En un negocio reciben periódicamente productos para la venta, se requiere desarrollar un programa de consola (o
terminal) que cumpla con los siguientes requerimientos:
1. Se requiere organizar el inventario en los siguientes grupos: dairy, cleaning y grain.
2. Cada grupo tiene que estar asociado a un elemento de otra lista que almacena las existencias de ese grupo en la
misma posición, como en el siguiente ejemplo:
dairy_products = [“Fairlife Milk”, “Alta Dena Milk”, “Queensland Butter”]
dairy_stock = [28, 36, 50]
En donde, por ejemplo, el producto del grupo dairy “Alta Dena Milk” tiene una existencia de 36 unidades.
3. Para un producto entrante, se debe poder registrar en el sistema: el nombre del producto, la cantidad y el grupo
al que pertenece.
4. Si el producto no existe en la lista, se debe agregar al final con su cantidad entrante, pero si existe se debe
actualizar el número de existencias sumando la nueva cantidad.
5. El programa debe permitir visualizar todo el inventario de productos y existencias.
