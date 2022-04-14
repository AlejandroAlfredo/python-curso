elements = []
valueOne = int(input("Escribe el numero de elementos: "))
i = int(input("Escribe el numero del multiplicador: "))
valueTwo = 0
for value in range(0, valueOne):
    resultado = (i * value)

    elements.append(resultado)
print(elements)