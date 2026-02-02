animals = ["dog", "goat", "cow", "cat", "parrot", "sparrow"]
for animal in animals:
    print(f"A {animal} would be a great pet.")
    
print(animals , "have four legs.")

print("The first three items in the list are: ")
for name in animals[0:3]:
    print(name)

print("The three items from the middle of the list are: ")
for name in animals[2:4]:
    print(name)
    
print("The last three items in the list are: ")
for name in animals[4:6]:
    print(name)