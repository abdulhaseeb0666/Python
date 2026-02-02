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