print("Hello" == "Hello")
print("Hello" == "hello")

str1 = "String"
str2 = "STRING"
print(str1 == str2)
print(str1.lower() == str2.lower())

print(5>10)
print(5>=10)
print(5<10)
print(5<=10)

print(5>10 and 5<10)
print(5>10 or 5<10)

home = ["USA", "Dubai", "Qatar", "Austrailia"]
if "USA" in home:
    print(True)
else:
    print(False)

if "Pakistan" not in home:
    print(False)