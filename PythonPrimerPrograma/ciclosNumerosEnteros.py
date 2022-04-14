#pedir 2 numero, hasta que el segundo sea mayor que el primero, al final mostrar los primeros numeros

def myNumeros (valueOne, valueTwo):

    while valueOne > valueTwo:
        valueTwo = int(input("Escribe el segundo numero: "))
    return valueTwo
valueOne = int(input("Escribe el primer numero: "))
valueTwo = int(input("Escribe el segundo numero: "))
resultado = myNumeros(valueOne, valueTwo)

print(str(valueOne) +" "+ str(resultado))