# pedir numero de alumnos
# pedir el nombre de cada alumno
# imprimir el array de alumnos
alumnos = []
valueOne = int(input("Escribe el numero de alumnos: "))

for value in range(0,valueOne):
    resultado = input("Cual es el nombre del alumno: ")

    alumnos.append(resultado)
print("-- Alumnos --")
print(alumnos)