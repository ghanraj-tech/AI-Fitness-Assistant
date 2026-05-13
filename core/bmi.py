def calculate_bmi(weight, height):

    bmi = weight / ((height / 100) ** 2)

    return round(bmi, 2)


def bmi_status(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"