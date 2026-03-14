while True:
    age = input("Please enter your age: ")
    if int(age) < 3:
        ticket_price = 0
    elif int(age) < 12:
        ticket_price = 10
    else:
        ticket_price = 15
    print(f"Your ticket price is ${ticket_price}.")