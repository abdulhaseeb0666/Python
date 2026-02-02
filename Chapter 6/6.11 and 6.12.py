cities = {
    'Multan': {
        'country': 'Pakistan',
        'population': 1800000,
        'facts': ['Known as the City of Saints due to its numerous Sufi shrines.',
                  'Famous for its mangoes and handicrafts.']
    },
    'Karachi': {
        'country': 'Pakistan',
        'population': 15000000,
        'facts': ['The largest city in Pakistan and a major economic hub.', 'Known for its diverse culture and cuisine.'] 
    },
    'Lahore': {
        'country': 'Pakistan',
        'population': 11000000,
        'facts': ['Famous for its historical sites and vibrant culture.', 'Known as the heart of Pakistan.']
    }
}

for city, details in cities.items():
    print(f"\nCity: {city}")
    print(f" --Country: {details['country']}")
    print(f" --Population: {details['population']}")
    print(" --Facts:")
    for fact in details['facts']:
        print(f"    - {fact}")