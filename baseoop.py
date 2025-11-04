# Create a class named Person
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

# Create a class named Student that inherits from Person
class Student(Person):
    pass

# Create an object of Student class
x = Student("K", "Perera")
x.printname()
