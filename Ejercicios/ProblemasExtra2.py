# pedir un string e imprimir cuantas veces se repite cada letra
def myMethodTwo(list, value):
    counter = 0
    valueTwo = input("Escribe la letra a buscar")
    list = value.replace(valueTwo, " ")
    for x in list:
        if(x == " "):
            counter = counter + 1
    print("la letra que escribio se repite: " + str(counter))

def myMethod(value, list):
    for x in value:
        list.append(x)
    myMethodTwo(list, value)
list = []
value = input("Escribe una cadena de texto: ")
myMethod(value, list)