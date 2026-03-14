peoples = ['alice', 'bob', 'charlie', 'david', 'eve']

peoples_languages = {
    'alice': 'python',
    'bob': 'java',
    'charlie': 'c++',
}

for person in peoples:
    if person in peoples_languages:
        language = peoples_languages[person].title()
        print(f"Thank you, {person.title()}, for taking the poll! You like {language}.")
    else:
        print(f"{person.title()}, please take our poll!")