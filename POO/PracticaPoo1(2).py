# pedir alumnos(n) y calcular su promedio de calificacion tomando encuenta que cursa 2 materias.
# Realizarlo usando POO
class Alumno:
    def __init__(self):
        self.nombre = input("Escribe el nombre del alumno: ")

    def materias(self):
        self.calificationMath = float(input("Escribe la calificacion de matematicas: "))
        self.calificationEnglish = float(input("Escribe la calificacion de ingles: "))

    def promedio(self):
        self.resultado = (self.calificationMath + self.calificationEnglish) / 2
        total[self.nombre] = self.resultado

flags = False
total = {}
while flags != True:
    options = int(input("-- menu --\n1.Agregar alumnos 2.Ver por promedio 3.salir\n--> "))
    if (options == 1):
            myAlumno = Alumno()
            myAlumno.materias()
            myAlumno.promedio()

    if(options == 2):
            print(total)

    if (options == 3):
            flags = True