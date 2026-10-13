def greet(name):
    return("what's up " + name)

print(greet("faushy"))

def calculatebmi(weight, height):
    bmi = 703 * weight / (height ** 2)
    return bmi

a=float(input("enter your weight in lbs: "))
b=float(input("enter your height in inches: "))
print("your bmi is: " + str(round(calculatebmi(a, b), 1)))
