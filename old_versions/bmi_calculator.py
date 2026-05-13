# AI Fitness BMI Calculator

name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

# BMI Formula
bmi = weight / (height ** 2)

print("\n----- FITNESS REPORT -----")
print("Name:", name)
print("Your BMI is:", round(bmi, 2))

# Fitness Category
if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal Weight")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")