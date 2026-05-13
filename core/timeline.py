def calculate_timeline(current_weight, target_weight):

    difference = abs(current_weight - target_weight)

    months = difference / 2

    return round(months, 1)