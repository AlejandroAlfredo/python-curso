# Escribe un programa que pida números enteros mientras sean cada vez más grandes.
valueOne = int(input("Escribe un numero: "))
valueTwo = int(input("Escribe un numero mayor a " + str(valueOne) + ": "))
while valueTwo > valueOne:
    valueOne = valueTwo
    valueTwo = int(input("Escribe un numero mayor a " + str(valueOne) + ": "))

print(""+ str(valueTwo) + " no es mayor que " + str(valueOne))