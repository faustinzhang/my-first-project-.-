def greet(name):
    return("what's up " + name)

print(greet("faushy"))

def calculatebmi(weight, height):
    bmi = 703 * weight / (height ** 2)
    return bmi

a=int(input("enter your weight in lbs: "))
b=int(input("enter your height in inches: "))
print("your bmi is: " + str(round(calculatebmi(a, b))))