# -*- coding: utf-8 -*-
"""PruebaGlobantEj4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xatr2miPJnaAYz7E5zrp7NUI6CLsNAiL

**Ejercicio 4**

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
"""

class Inventario():
  def __init__(self):
    #Inicializar todas las listas
    self.dairy_products_ = []
    self.dairy_stock_ = []
    self.cleaning_products_ = []
    self.cleaning_stock_ = []
    self.grain_products_ = []
    self.grain_stock_ = []

  def comprobar(self, lista, producto):
    #Comprobar si el producto está en la lista indicada
    if lista == 1:
      return producto in self.dairy_products_
    elif lista == 2:
      return producto in self.cleaning_products_
    elif lista == 3:
      return producto in self.grain_products_
    return False

  def agregarProducto(self, lista, nombre, stock):
    #Comprobar si el producto está en la lista indicada
    if self.comprobar(lista, nombre):
      #Si el producto está, buscar su posición en la lista de los nombres
      #y actualizar el stock en la lista de stocks en la posición correspondiente
      if lista == 1:
        self.dairy_stock_[self.dairy_products_.index(nombre)] = stock
      elif lista == 2:
        self.cleaning_stock_[self.cleaning_products_.index(nombre)] = stock
      elif lista == 3:
        self.grain_stock_[self.grain_products_.index(nombre)] = stock
      return True

    else:
      #Si no está, añadir el producto y el stock en las listas correspondientes
      if lista == 1:
        self.dairy_products_.append(nombre)
        self.dairy_stock_.append(stock)
      elif lista == 2:
        self.cleaning_products_.append(nombre)
        self.cleaning_stock_.append(stock)
      elif lista == 3:
        self.grain_products_.append(nombre)
        self.grain_stock_.append(stock)
      return False

  def verInventario(self, lista):
    #Retornar los productos y el stock del tipo de producto indicado
    if lista == 1: return (self.dairy_products_, self.dairy_stock_)
    elif lista == 2: return (self.cleaning_products_, self.cleaning_stock_)
    elif lista == 3: return (self.grain_products_, self.grain_stock_)

def agregarProducto(inv: Inventario):
  introduccion = "Agregar Producto"
  print("\n",introduccion,"\n","-"*len(introduccion))

  #Ingresar el nombre del producto
  print("Ingrese el nombre del producto: ")
  nombre = input()

  #Ingresar la cantidad en stock del producto
  print("Ingrese la cantidad en stock: ")
  stock = int(input())

  #Ingresar el tipo de producto
  op = 0
  while op not in (1, 2, 3):
    print("Seleccione el tipo de producto: ")
    print("1. Dairy\n2. Cleaning\n3. Grain")
    print("\nSu opcion: ")
    op = int(input())
    if op not in (1, 2, 3): print("Opcion no valida. Por favor ingrese una de las opciones mostradas.\n")

  #Agregar producto
  resp = inv.agregarProducto(op, nombre, stock)
  print("Producto Modificado") if resp else print("Producto Agregado")

def verInventario(inv: Inventario):
  #Ingresar el tipo de producto
  introduccion = "Ver reporte de inventario"
  print("\n",introduccion,"\n","-"*len(introduccion))

  op = 0
  while op not in (1, 2, 3):
    #Seleccionar el tipo de producto
    print("Seleccione el tipo de producto: ")
    print("1. Dairy\n2. Cleaning\n3. Grain")
    print("\nSu opcion: ")
    op = int(input())
    if op not in (1, 2, 3): print("Opcion no valida. Por favor ingrese una de las opciones mostradas.\n")

  #Consultar la lista de productos y la lista de stock
  productos, stock = inv.verInventario(op)

  #Imprimir
  print('{0:28} {1:12}'.format("Nombre", "Existencias"),"\n",'-'*40)
  for prod, num in zip(productos, stock):
    print(f'{prod:28} {num:12}')

#Inicio del programa
#Iniciallización de variables
inventario = Inventario()

while True:
  #Seleccionar una opción entre 1 y 3
  op = 0
  while op not in (1, 2, 3):
    introduccion = "Sistema de inventario. Ingrese una opcion:"
    print("\n",introduccion,"\n","-"*len(introduccion))
    print("1. Agregar producto")
    print("2. Ver reporte de inventario")
    print("3. Salir")
    print("\nSu opcion: ")
    op = int(input())
    if op not in (1, 2, 3): print("Opcion no valida. Por favor ingrese una de las opciones mostradas.\n")
    elif op == 1:
      agregarProducto(inventario)
    elif op == 2:
      verInventario(inventario)
    elif op == 3: break
  if op == 3: break

