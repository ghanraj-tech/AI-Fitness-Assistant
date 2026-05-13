# AI Diet Recommendation System

print("----- AI FITNESS DIET SYSTEM -----")

name = input("Enter your name: ")

weight = float(input("Enter your weight (kg): "))

height = float(input("Enter your height (m): "))

goal = input("Enter your goal (fatloss/musclegain/maintenance): ").lower()

# BMI Calculation
bmi = weight / (height ** 2)

# Protein Recommendation
protein = weight * 2

# Water Recommendation
water = weight * 0.04

print("\n----- FITNESS REPORT -----")

print("Name:", name)

print("BMI:", round(bmi, 2))

print("Recommended Protein Intake:", round(protein), "grams/day")

print("Recommended Water Intake:", round(water, 2), "litres/day")

# Goal Based Recommendations
if goal == "fatloss":

    print("\nDIET PLAN:")
    print("- High protein diet")
    print("- Low sugar intake")
    print("- Eat in calorie deficit")

    print("\nWORKOUT:")
    print("- Cardio 4-5 times/week")
    print("- Weight training")

elif goal == "musclegain":

    print("\nDIET PLAN:")
    print("- High protein + high carbs")
    print("- Calorie surplus diet")
    print("- Eat every 3-4 hours")

    print("\nWORKOUT:")
    print("- Heavy weight training")
    print("- Progressive overload")

else:

    print("\nDIET PLAN:")
    print("- Balanced healthy diet")
    print("- Maintain calories")

    print("\nWORKOUT:")
    print("- Moderate exercise")
    print("- Mix cardio + weights")