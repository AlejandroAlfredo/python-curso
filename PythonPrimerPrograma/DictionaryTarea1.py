# 1.Pedir 5 alumnos y almacenar sus calificaciones en un diccionario.
# validar y hasta que exista.
myAlumnos = {}
for x in range(0,5):
    valueName = input("Escribe el nombre del alumno: ")
    valueDatos = int(input("Escribe la calificacion: "))
    myAlumnos[valueName] = valueDatos
print(myAlumnos)

for x,y in myAlumnos.items():
    if(y > 70):
        print(x)
for x,y in myAlumnos.items():
    valueName = input("Escribe el nombre del alumno: ")
    if(valueName in myAlumnos):
        print("este alumnno existe")
        exit()
    if(valueName != myAlumnos):
        print("no existe ese alumno")
        continue