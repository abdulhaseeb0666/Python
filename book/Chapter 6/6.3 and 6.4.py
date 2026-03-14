glossary = {
    "if statement": "A conditional statement that executes a block of code if a specified condition is true.",
    "else statement": "A block of code that executes if the condition in the if statement is false.",
    "elif statement": "A conditional statement that checks another condition if the previous if statement was false.",
    "for loop": "A control flow statement that iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence.",
    "while loop": "A control flow statement that repeatedly executes a block of code as long as a specified condition is true.",
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n\t{definition}\n") 