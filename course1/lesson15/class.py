# clasees are like a blueprint for creating objects
# they define the attributes and methods that objects of that class will have
# the self argument is a reference to the object itself. it is used to access the attributes and methods of the class within the class definition

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")
    def sayAge(self):
        print(f"I am {self.age} years old")


emaka = Person("Emaka", 25)
emaka.greet()
        
# class inheritance
# this is a way to create a new class that inherits the attributes and methods of an existing class

class Student(Person):

    def sayClass(self):
        print(f"i am a student")

obi = Student("Obi", 20)
obi.greet()
obi.sayClass()

# if the new class wont have any new attributes or methods, we can use the pass keyword to indicate that the class is empty

class EmptyClass(Person):
    pass

ss1 = EmptyClass("john", 20)
ss1.greet()
ss1.sayAge()

# if the new class has only new attributes or methods, we can use the super() function to call the parent class

class ManPerson(Person):
    def __init__(self, name, age, number_of_wives):
        super().__init__(name, age)
        self.number_of_wives = number_of_wives
        
    def sayNumberOfWives(self):
        print(f"I have {self.number_of_wives} wives")



agu = ManPerson("Agu", 30, 2)
agu.greet()
agu.sayNumberOfWives()


# polymorphism is the ability of different classes to be treated as instances of the same class through inheritance. it allows us to use a single interface to represent different types of objects

class WomanPerson(Person):
    def __init__(self, name, age, number_of_kids):
        super().__init__(name, age)
        self.number_of_kids = number_of_kids

    def sayAge(self):
        print(f"I am woman of, {self.age} years old and I have {self.number_of_kids} kids")

sarah = WomanPerson("Sarah", 25, 3)
sarah.sayAge()


for v in (sarah, agu, emaka, ss1):
    v.sayAge()