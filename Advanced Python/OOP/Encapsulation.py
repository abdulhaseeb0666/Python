class Person:
    def __init__(self, rollno, _name, __age):
        self.rollno = rollno     #Public   
        self._name = _name     #Protected : NO Functionality, just a convention
        self.__age = __age     #Private
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

person1 = Person("Alice", 30)
# print(person1.__name)              # This will raise an AttributeError
print(person1.get_name())
print(person1.get_age())