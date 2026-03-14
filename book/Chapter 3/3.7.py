names = ["Alice", "Bob", "Charlie"]
guest1 = "David"
guest2 = "Frank"
guest3 = "Jack"
names.insert(0, guest1)
names.insert(3, guest2)
names.append(guest3)
cannotCome="Bob"

for name in names:
    if name == cannotCome:
        name = "Jane"
    print(f"Dear " + name + ", you are invited to the party.")
    
print("\nUnfortunately, I can only invite two people for dinner.\n")

while len(names) > 2:
    removed = names.pop()
    print(f"Dear {removed}, I'm sorry I can't invite you to dinner.")

print("\nThe following people are still invited:")
for name in names:
    print(f"Dear {name}, you are still invited to dinner.")

del names[-2:]
print("\nFinal guest list:", names)