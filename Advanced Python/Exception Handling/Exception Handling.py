a = int(input("Enter a number: "))

#  If the user enters zero, it will raise a ZeroDivisionError when we try to divide by it. We can handle this exception using a try-except block.
try:
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

b = int(input("Enter another number: "))

try:
    result = 10 / b
    print("Result:", result)
except Exception as err:
    print("Sorry there is an error:", err) 
else:
    print("The division was successful, no exceptions were raised.")
finally:
    print("I will print no matter what.")

print("This will always be printed, regardless of whether an exception occurred or not.")