#operaciones con funciones
def mySuma(valueOne, valueTwo):
        operations = valueOne + valueTwo
        return operations

def myResta(valueOne, valueTwo):
        operations = valueOne - valueTwo
        return operations

def myMultiplicacion(valueOne, valueTwo):
        operations = valueOne * valueTwo
        return operations

def myDivision(valueOne, valueTwo):
        operations = valueOne / valueTwo
        return operations

print("\nMenu de operaciones")
options = int(input("Elige una opcion: \n1.Suma 2.Resta 3.Multiplicacion 4.Division\n"))
valueOne = int(input("Escribe el primer valor: "))
valueTwo = int(input("Escribe el segundo valor: "))
operations = 0
if(options == 1):
    print("\n-- suma --")
    operations = mySuma(valueOne, valueTwo)

if(options == 2):
    print("\n-- resta --")
    operations = myResta(valueOne, valueTwo)

if(options == 3):
    print("\n-- multiplicacion --")
    operations = myMultiplicacion(valueOne, valueTwo)

if(options == 4):
    print("\n-- division --")
    operations = myDivision(valueOne, valueTwo)

print("El resultado es: " + str(operations))