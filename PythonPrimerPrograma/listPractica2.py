# Ejercicio 2.
# 1. pedir un numero al usuario y crear su tabla.
#  de multiplicador en una lista, imprimir la lista.
def myFuncion(valueOne, myTable):
    for x in range(1,101):
        myTable.append(valueOne * x)
    return myTable
myTable = []
valueOne = int(input("para crear tu tabla escribe un numero: "))
resultado = myFuncion(valueOne, myTable)
print(resultado)