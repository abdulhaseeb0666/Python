a = [1,2,3,4,5]


# Maps

print("Using map with Normal function:")
def double(x):
    return x**2
result1 = map(double, a)
print(list(result1))

print("Using map with a lambda function:")
result2 = map(lambda x: x**2, a)
print(list(result2))


# Filter
print("\nUsing filter with Normal function:")
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

result3 = filter(is_even, a)
print(list(result3))

print("Using filter with a Lambda function:")
result4 = filter(lambda x: x % 2 == 0, a)
print(list(result4))
