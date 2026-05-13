def get_workout_plan(goal):

    if goal == "Weight Loss":

        return [

            "Running",
            "Cycling",
            "Jump Rope",
            "HIIT",
            "Pushups"
        ]

    elif goal == "Muscle Gain":

        return [

            "Bench Press",
            "Deadlift",
            "Squats",
            "Pullups",
            "Shoulder Press"
        ]

    else:

        return [

            "Walking",
            "Stretching",
            "Yoga"
        ]