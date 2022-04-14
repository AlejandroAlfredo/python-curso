# 1. hacer programa utilizando POO para el control de almacen
# -Registrar producto (nombre existencia)
# -Realizar venta y descontar de almacen
# -Agregar entradas de producto
# con menu 1.Registrar 2.Vender 3.Entrada
class Almacen:
    def myRegistrar(self):
        nombre = input("Escribe el nombre del producto: ")
        if(nombre in product):
            for x,y in product.items():
                if(x in nombre):
                    print(x,"en Existencia: " + str(y))
        else:
            print("Ese producto no existe")

    def myVender(self):
        nombre = input("Escribe el nombre del producto : ")
        if(nombre in product):
            for x, y in product.items():
                if (x in nombre):
                    y
            cantidad = int(input("Escriba la cantidad que usted desea del producto: "))
            if(cantidad <= y):
                resultado = y - cantidad
                product[nombre] = resultado
                if (resultado == 0):
                    product.pop(nombre)
            if(cantidad > y):
                print("No podemos vender esa cantidad, ahora volvera al inicio.")
        else:
            print("Ese producto no esta disponible, lo sentimos.")

class Productos:
    def myEntrada(self):
        nombre = input("Escribe el nombre del producto: ")
        cantidad = int(input("Escribe la nueva cantidad producto: "))
        product[nombre] = cantidad

product = {}
nombre = ""
cantidad = 0
flags = False
while flags != True:
    try:
        options = int(input("-- control de almacen --\n1.Registrar 2.Vender 3.Entrada a productos\n--> "))
        if(options == 1):
            myAlmacen = Almacen()
            myAlmacen.myRegistrar()
        if(options == 2):
            myAlmacen = Almacen()
            myAlmacen.myVender()
        if(options == 3):
            myProductos = Productos()
            myProductos.myEntrada()
    except:
        print("\n--> Elige una opcion correcta, datos incorrectos no se guardaran <--\n")