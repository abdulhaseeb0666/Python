class Bag():
    price = 1000
    def __init__(self , material , pocket , color):
        self.material = material
        self.pocket = pocket
        self.color = color


    # It is an instance method
    def show(self):
        print(f"Material: {self.material} , Pocket: {self.pocket} , Color: {self.color}")


    # Class method takes a class as parameter and it cannot access instance attributes but it can access class attributes and other class methods. It is used to create factory methods.
    @classmethod
    def from_string(cls):
        print("It is a class method")
        # Below code will Work because it is a class attribute
        print(cls.price)
        # Below code will not work because it is an instance attribute. So is commented out.    
        #   print(cls.material)


    # Static method does not take any parameter and it cannot access instance attributes and class attributes. It is used to create utility methods. 
    @staticmethod
    def is_bag():
        print("It is a static method")
        # Below code will not work because it is an instance attribute. So is commented out.    
        #   print(cls.material)
        # Below code will not work because it is a class attribute. So is commented out.    
        #   print(cls.price)


reebok = Bag("Leather" , 3 , "black")
Balenciaga = Bag("Gold" , 5 , "red")
reebok.show()
Balenciaga.show()

reebok.from_string()
reebok.is_bag()