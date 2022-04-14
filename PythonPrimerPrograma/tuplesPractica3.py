# 2.Pedir una cadena por teclado, e insertar cada letra en una tupla.
def myFuncion(valueOne,tuple,list):
    for x in valueOne:
        list.append(x)
        tuple = list
    return tuple
list = []
tuple = ()
valueOne = input("Escribe una palabra: ")
resultado = myFuncion(valueOne,tuple,list)
print(resultado)