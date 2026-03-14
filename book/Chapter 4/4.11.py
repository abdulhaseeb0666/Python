myPizzaz = ['pepperoni', 'margherita', 'bbq chicken', 'hawaiian']
frindsPizzaz = myPizzaz[:]

myPizzaz.append("veggie lover")
frindsPizzaz.append("meat lover")

print("My favourite pizzas are: ")
for pizza in myPizzaz:
    print(pizza)
    
print("\nMy Friend's favourite pizzas are: ")
for pizza in frindsPizzaz:
    print(pizza)