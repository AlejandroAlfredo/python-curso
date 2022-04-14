# 1.Crea una tupla con numeros, pedir al usuario un numero e indicar cuantas veces esta el numero en la tupla.
def myFuncion(valueOne, myTuples):
    counter = 0
    for x in myTuples:
        if(valueOne == x):
            counter = counter + 1
    return counter
myTuples= (1,2,2,3,3,3,4,4,4,4)
valueOne = int(input("Escribe un numero: "))
resultado = myFuncion(valueOne, myTuples)

print(resultado)