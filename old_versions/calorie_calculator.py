# AI Fitness Calorie Calculator

print("----- DAILY CALORIE CALCULATOR -----")

age = int(input("Enter your age: "))

weight = float(input("Enter your weight (kg): "))

height = float(input("Enter your height (cm): "))

gender = input("Enter gender (male/female): ").lower()

# BMR Calculation
if gender == "male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

print("\nYour BMR is:", round(bmr, 2))

# Activity Level
print("\nSelect Activity Level:")
print("1. Sedentary")
print("2. Lightly Active")
print("3. Moderately Active")
print("4. Very Active")

choice = int(input("Enter choice (1-4): "))

if choice == 1:
    calories = bmr * 1.2

elif choice == 2:
    calories = bmr * 1.375

elif choice == 3:
    calories = bmr * 1.55

else:
    calories = bmr * 1.725

print("\n----- CALORIE REPORT -----")

print("Maintenance Calories:", round(calories))

print("Fat Loss Calories:", round(calories - 400))

print("Muscle Gain Calories:", round(calories + 300))