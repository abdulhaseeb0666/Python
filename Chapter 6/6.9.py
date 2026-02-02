favourite_places = {
    'alice': ['paris', 'new york'],
    'bob': ['tokyo'],
    'charlie': ['london', 'berlin', 'rome'],
}

for person, places in favourite_places.items():
    print(f"\n{person.title()}'s favourite places are:")
    for place in places:
        print(f"- {place.title()}")