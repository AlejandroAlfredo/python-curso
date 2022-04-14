# 1. Agregar los numeros del 1 al 100 en una lista, imprimir la lista
def myFuncion(myNumeros):
    for x in range(1, 101):
        myNumeros.append(x)
    return myNumeros
myNumeros = []
resultado = myFuncion(myNumeros)
print(resultado)