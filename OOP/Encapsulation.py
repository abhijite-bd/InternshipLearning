# Encapsulation is defined as binding together the data and the functions that manipulate them.
class Book:
    def __init__(self):
        pass
    def setName(self,name):
        self.name=name
    def printName(self):
        print(self.name)
b1=Book()
b1.setName("Skin Cancer Detection")
b1.printName()
print(b1.name)