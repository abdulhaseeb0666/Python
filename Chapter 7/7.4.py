pizzaToppings = input("Enter a pizza topping (or 'quit' to finish): ")
while pizzaToppings.lower() != 'quit':
    print(f"Adding {pizzaToppings} to your pizza.")
    pizzaToppings = input("Enter a pizza topping (or 'quit' to finish): ")
print("Finished making your pizza!")