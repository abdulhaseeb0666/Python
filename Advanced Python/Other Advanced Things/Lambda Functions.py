def addition(a,b):
    print(a+b)

addition(5,10)

# Above is a normal function, but we can also do the same thing with a lambda function.
print("Using a lambda function:")
addition_lambda = lambda a,b: print(a+b)
addition_lambda(5,10)

# Example

even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(15))