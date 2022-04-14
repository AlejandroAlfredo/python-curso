# Tarea 1
# Mutations.
# pedir un string, cambiar la letra en la posicion indicada e imprimir el nuevo string.
myList = []
valueOne = input("Escribe una palabra: ")
for x in valueOne:
    myList.append(x)
dirOne = myList.copy()
print(myList)
myList.clear()

for x in range(len(valueOne)):
    myList.append(x)
print(myList)
myList.clear()

valueTwo = int(input("Escribe la posision de la letra por cambiar: "))
value = input("Escribe la nueva letra: ")
dirOne[valueTwo] = value
print("".join(dirOne))