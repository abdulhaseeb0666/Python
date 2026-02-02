age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:  
    price = 40
else:
    price = 20

price=str(price)
print("Your admission cost is " + price)
