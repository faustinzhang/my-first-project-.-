def greet(name):
    return("what's up " + name)

print(greet("faushy"))

def calculatebmi(weight, height):
    bmi = 703 * weight / (height ** 2)
    return bmi

a=float(input("enter your weight in lbs: "))
b=float(input("enter your height in inches: "))
bmi=calculatebmi(a, b)
print("your bmi is: " + str(round(bmi, 1)))

if bmi > 30:
    print("you are obese")
elif bmi > 25: 
    print("you are overweight")
elif bmi > 18.5:
    print("you are normal")
else:
    print("you are underweight")