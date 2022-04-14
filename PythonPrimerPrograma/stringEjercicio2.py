# 1. indicar si el numero de tarjetas valido
# plus pedir el ccv
def myMethod(valueTwo):
    value3 = input("Confirma tu ccv")
    if(value3 in valueTwo):
        print("esta tarjeta es valida.")
    else:
        print("Error!, esta tarjeta no es valida.")

newList = []
list = []
print("Debes agregar espacio tras escribir 4 numeros")
value = input("Escribe el numero de tu tarjeta: ")
for x in value:
    newList.append(x.isalpha())
if(True in newList):
    print("Error!, debes escribir solo digitos")
    exit()
if(len(value) > 19):
    print("Error!,tienes mas de 16 digitos")
    exit()
if(len(value) < 19):
    print("Error!,tienes menos de 16 digitos")
    exit()
list = value.split(" ")
listCopy = list.copy()
print("-".join(list))
if(len(list) == 4):
    print("Correcto su tarjeta tiene todos los datos")
    valueTwo = input("Escribe tu ccv: ")
    myMethod(valueTwo)

if(len(list) < 4):
    print("Error!, su tarjeta no tiene todo los digitos")
    exit()