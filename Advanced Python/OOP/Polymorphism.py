class Animal:
    def show(self):
        print("I am an animal")

class Dog(Animal):
    def show(self):
        print("I am a dog")

dog1 = Dog()
dog1.show()