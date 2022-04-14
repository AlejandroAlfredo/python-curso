class Person:
    def __init__(self,name, edad = 0):
        self.name = name
        self.edad = edad

    def myFun(self):
        print("Hola mi nombre es: " + self.name)
    def myFun2(self):
        print("Hola mi nombre es: " + self.name + " y la edad es: " + str(self.edad))

#p1 = Person("Jesus", 99)
p2 = Person("Ale")
#p1.myFun()
#p1.myFun2()
p2.myFun()
#p2.myFun2()