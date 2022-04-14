def solution(s):
    newName=""
    counter=0
    for value in s:
        if (counter == 0) :

            newName = newName + value.upper()

            counter = counter + 1
            continue

        if (value == " "):
            newName = newName + " "
            counter = 0
            continue
        else:
            newName= newName + value
            counter = counter + 1
    return newName

newName = solution(input("Escribe tu nombre: "))
print(newName)

