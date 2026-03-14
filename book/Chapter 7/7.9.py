sandwich_Orders = ["Tuna Sandwich","Pastrami Sandwich", "Chicken Sandwich","Pastrami Sandwich", "Veggie Sandwich", "Turkey Sandwich", "Pastrami Sandwich"]
finished_Sandwiches = []

while sandwich_Orders:
    current_Sandwich = sandwich_Orders.pop()
    if current_Sandwich == "Pastrami Sandwich":
        print("Sorry, we are out of Pastrami Sandwiches.")
        continue
    print(f"Making your {current_Sandwich}.")
    finished_Sandwiches.append(current_Sandwich)

print("\nFollowing sandwiches are made:")
for sandwich in finished_Sandwiches:
    print(f"- {sandwich}")