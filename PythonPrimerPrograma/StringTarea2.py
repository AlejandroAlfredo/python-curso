# pedir substring
# imprimir cuantas veces esta el substring
list = []
value = input("Ecribe algo: ")
for x in value:
    list.append(x)
valueTwo = input("buscar: ")
list = value.replace(valueTwo, " ")
counter = 0
for x in list:
    if(x == " "):
        counter = counter + 1
print(value)
print(counter)