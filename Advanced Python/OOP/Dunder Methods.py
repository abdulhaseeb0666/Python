class Animal:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def __add__(self, other):
        sum=0
        for i in other:
            sum+=i.age
        return f"The sum of ages are: {self.age + sum}"
    
obj1 = Animal("Dog", 5)
obj2 = Animal("Cat", 3)
obj3 = Animal("Bird", 2)

print(obj1)  #__str__ method will be called
print(obj2)  #__str__ method will be called
print(obj1 + [obj2])  #__add__ method will be called
print(obj1 + [obj2, obj3])  #__add__ method will be called