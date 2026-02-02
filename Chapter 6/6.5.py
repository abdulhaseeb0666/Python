rivers = {
    'nile': 'egypt',
    'indus': 'pakistan',
    'ganga': 'india',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")