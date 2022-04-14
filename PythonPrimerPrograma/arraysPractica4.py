# pedir un numero de alumnos
# pedir los alumnos y guardar en un arrays
# Luego
# pedir el nombre de un alumno a buscar
# si* el alumno existe imprimir
# si no* imprimir "no existe el alumno"
alumnos = []
valueOne = int(input("Escribe un numero de alumnos: "))
for value in range(0,valueOne):
    resultado = input("Escribe el nombre del alumno: ")
    alumnos.append(resultado)

valueTwo = input("Escribe el nombre del alumno a buscar: ")

for value in alumnos:
    if(valueTwo == value):
        print(valueTwo)
        exit()

print("No existe el alumno")