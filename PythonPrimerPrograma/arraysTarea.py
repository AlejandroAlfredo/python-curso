# pedir numero de alumnos
# pedir lista de alumnos (y llegar a un array)
# preguntar si quiere agregar o remover un alumno
# si es agregar, agregar
# si es remover, remover del array
# imprimir array
alumnos = []
numAlumnos = int(input("Escribe el numero de alumnos: "))
for i in range(0,numAlumnos):
    resultado = input("Escribe el nombre del alumno: ")
    alumnos.append(resultado)

options = int(input("quiere agregar o remover un alumno?: \n1.agregar 2.remover"))
if(options == 1):
    resultado = input("Escribe el nombre del alumno: ")
    alumnos.append(resultado)
if(options == 2):
    resultado = input("Escribe el nombre del alumno: ")
    alumnos.remove(resultado)
print("-- Alumnos --")
print(alumnos)