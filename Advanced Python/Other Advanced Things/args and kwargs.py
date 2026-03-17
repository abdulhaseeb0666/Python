def addition(a,b):
    print(f"Simple Addition: {a+b}")

addition(5, 3)

# But id the number of arguments is not fixed then we can use *args and **kwargs

def additionWithArgs(*args):    
    sum=0
    for i in args:
        sum+=i
    print(f"Addition with Args: {sum}")

additionWithArgs(1,3,5,7,9)
additionWithArgs(1, 2, 3, 4, 5,24543245,32452345,32453245,325,34253245,32452345,2345,32453,245235,234525)


# Key Word Arguments(**kwargs)
def additionWithKwargs(**kwargs):
    sum=0
    for i in kwargs.values():
        sum+=i
    print(f"Addition with Kwargs: {sum}")

additionWithKwargs(a=1, b=3, c=5, d=7, e=9)
additionWithKwargs(a=1, b=2, c=3, d=4, e=5, f=24543245, g=32452345, h=32453245, i=325, j=34253245, k=32452345, l=2345, m=32453, n=245235, o=234525)


def additionWithArgsAndKwargs(*args, **kwargs):
    sum=0
    for i in args:
        sum+=i
    for i in kwargs.values():
        sum+=i
    print(f"Addition with Args and Kwargs: {sum} \n")

additionWithArgsAndKwargs(1,3,5,7,9, a=1, b=3, c=5, d=7, e=9)

def displayInfo(**kwargs):
    print("Displaying Information:")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")
    print("\n")
    
displayInfo(name="Haseeb", age=20, city="Multan")


def argsAndKwargsInDecorators(func):
    print("This is a decorator function that can handle both *args and **kwargs.\n")
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.\n")
    return wrapper

@argsAndKwargsInDecorators
def displayInfoWithDecorators(*args , **kwargs):
    print("Displaying Args:")
    for i in args:
        print(i)
    print("Displaying Kwargs:")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")
 
displayInfoWithDecorators(12,4234,123)
displayInfoWithDecorators("Hello", "World", name="Haseeb", age=20, city="Multan")
displayInfoWithDecorators(name="Haseeb", age=20, city="Multan")
