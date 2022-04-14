# pedir numero de elementos
# pedir cada elemento y agregarlo al array
# crear o imprimir un nuevo array con los numeros mayores a (5)
numeros = []
mayores = []
valueOne = int(input("Escribe el numero de elementos: "))
for value in range(0,valueOne):
    resultado = int(input("Escribe un numero: "))
    if(resultado > 5):
        numerosMayores = resultado
        mayores.append(resultado)

    numeros.append(resultado)
print("-- mayores a 5 --")
print(mayores)