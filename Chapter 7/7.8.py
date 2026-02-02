sandwich_Order = ["Tuna Sandwich", "Chicken Sandwich", "Veggie Sandwich", "Turkey Sandwich"]
finished_Sandwiches = []

while sandwich_Order:
    current_Sandwich = sandwich_Order.pop()
    print(f"Making your {current_Sandwich}.")
    finished_Sandwiches.append(current_Sandwich)

print("\nFollowing sandwiches are made:")
for sandwich in finished_Sandwiches:
    print(f"- {sandwich}")