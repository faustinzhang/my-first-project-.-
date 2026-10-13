name = input("What is your name? ").lower()
if name == "faushy":
    print("ouu shiii it's daddy " + name + "!")
else:
    print("Hey " + name + ", welcome to the program!")

age = input("How old are you? ")
while not age.isdigit():
    print("pls enter a valid age.")
    age= input("how old ru? ")
if int(age) < 18:
    print("You are not an adult")
else:
    print("ur a frickin adult")