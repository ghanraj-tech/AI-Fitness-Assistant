def calculate_calories(gender, weight, height, age, activity):

    if gender == "Male":

        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    else:

        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multipliers = {

        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725
    }

    calories = bmr * activity_multipliers[activity]

    return round(calories, 2)