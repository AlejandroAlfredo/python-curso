# pedir una lista de numeros(preguntar cuantos) y recuperar el mayor y menor
def myProceso(list,value):
    list.append(value)
    while value > 0:
        value = int(input("(Escribe 0 para terminar.)Escribe un numero: "))
        list.append(value)
    list.sort(reverse=True)
    return list
list = []
value = int(input("(Escribe 0 para terminar.)Escribe un numero: "))
newList = myProceso(list, value)
print("-- resultados --")
print("El numero mayor es: " + str(newList[0]))
final = len(newList) - 1
print("El numero menor es: " + str(newList[final]))