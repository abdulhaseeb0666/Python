peopleNumber = input("How many people are in your dinner group? ")
peopleNumber = int(peopleNumber)
if peopleNumber > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")