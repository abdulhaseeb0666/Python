names = ["Alice", "Bob", "Charlie"]
cannotCome="Bob"
for name in names:
    if name == cannotCome:
        name="David"
    print("Dear " + name + ", you are invited to the party.")