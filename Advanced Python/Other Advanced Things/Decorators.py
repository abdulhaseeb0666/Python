def decorate(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.\n")
    return wrapper

@decorate
def hello():
    print("Hello, World!")

hello()


# _________________________________________________________________________________________________________

def add_decorator(func):
    def wrapper(x, y):
        print("The sum is being calculated.")
        result = func(x, y)
        print("Thank you for using our calculator.")
        return result
    return wrapper

@add_decorator
def add(x, y):
    print(f"The sum of {x} and {y} is: {x + y}")

add(5, 3)

