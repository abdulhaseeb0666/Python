favourite_numbers = {
    'alice': [3, 7, 9],
    'bob': [2, 4],
    'charlie': [1, 5, 8, 12],
}

for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"- {number}")