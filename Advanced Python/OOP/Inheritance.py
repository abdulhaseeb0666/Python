class Animal:  #It is the parent class or base class
    legs = 4
    
    def __init__(self, name):
        self.name = name

    def show(self):
        return (f"I am {self.name} \n")
    
class Dog(Animal): #It is the child class or derived class
    def __init__(self, name , age ):
        super().__init__(name) #This line calls the __init__ method of the parent(Super) class (Animal) to initialize the name attribute
        self.age = age
    def show(self):
        return (f"I am {self.name} and my age is {self.age}. \n")

animal1 = Animal("Lion") #Creating an instance of the Animal class
print(animal1.name)
print(animal1.legs)
print(animal1.show())

# both animal and dog have their own show method
dog1 = Dog("Buddy" , 5) #Creating an instance of the Dog class, which inherits from the Animal class
print(dog1.name)
print(dog1.legs)
print(dog1.age)
print(dog1.show())


# __________________________________________________________________________________________________

# Multiple Inheritance:
class Father:
    roles1 = "Provider"
    def skills(self):
        return "Gardening, Programming"
    
class Mother:
    roles2 = "Caretaker"
    def skills(self):
        return "Cooking, Cleaning"
    
class Child1(Father, Mother): #The Child class inherits from both Father and Mother classes
    def skills(self):
        return "Inherits skills from both parents: " + Father.skills(self) + " and " + Mother.skills(self) + "\n"
    
child1 = Child1() #Creating an instance of the Child class
print(child1.roles1) #Accessing the roles1 attribute from the Father class
print(child1.roles2) #Accessing the roles2 attribute from the Mother class
print(child1.skills())

# __________________________________________________________________________________________________

# Multilevel Inheritance:
class Grandfather:
    def legacy(self):
        return "Wealth and Wisdom"
    
class Father(Grandfather):
    def profession(self):
        return "Engineer"
    
class Child2(Father):
    def hobbies(self):
        return "Playing and Coding \n"

child2 = Child2() #Creating an instance of the Child class
print(child2.legacy()) #Accessing the legacy method from the Grandfather class
print(child2.profession()) #Accessing the profession method from the Father class
print(child2.hobbies())

# Example 2 of Multilevel Inheritance:

class Factory:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"Factory Name: {self.name}"
    
class Vehicle(Factory):
    def __init__(self, name, model):
        super().__init__(name) #Calling the __init__ method of the Factory class to initialize the name attribute
        self.model = model

    def show(self):
        return f"Factory Name: {self.name}, Vehicle Model: {self.model}"
    
class Car(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model) #Calling the __init__ method of the Vehicle class to initialize the name and model attributes
        self.year = year

    def show(self):
        return f"Car Name: {self.name}, Car Model: {self.model}, Year: {self.year}"

bmw1 = Car("BMW ", "X5", 2022) #Creating an instance of the BMW class
print(bmw1.show()) #Accessing the show method of the BMW class, which overrides the show method of the Car class and the Factory class

# __________________________________________________________________________________________________

