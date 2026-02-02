locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print("Original List: ", locations)
print("Sorted List: ", sorted(locations))
print("Still original list:", locations)
print("Reverse Sorted List: ", sorted(locations, reverse=True))
print("Still original list:", locations)
locations.reverse()
print("Reversed List: ", locations)
# print("Reversed List: ", locations)