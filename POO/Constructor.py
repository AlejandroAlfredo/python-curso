# Constructor
class Person:
    def __init__(self, name):
        self.name = name
    def myFun(self):
        print("Hola mi nombre es: " + self.name)

p1 = Person("Jesus")
p2 = Person("Ale")
p1.myFun()
p2.myFun()