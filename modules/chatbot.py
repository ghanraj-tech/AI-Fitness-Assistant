def get_fitness_response(user_input: str):

    user_input = user_input.lower()

    # ---------- BMI ---------- #

    if "bmi" in user_input:
        return """
📊 BMI (Body Mass Index)

BMI helps measure body fat using height and weight.

BMI Range:
- Underweight = Below 18.5
- Normal = 18.5 – 24.9
- Overweight = 25 – 29.9
- Obese = 30+

Maintaining a normal BMI helps improve overall fitness.
"""

    # ---------- FAT LOSS ---------- #

    elif (
        "fat loss" in user_input
        or "lose weight" in user_input
        or "weight loss" in user_input
        or "burn fat" in user_input
    ):

        return """
🔥 FAT LOSS PLAN

✅ Eat high protein foods
(eggs, chicken, paneer, dal)

✅ Reduce sugar & junk food

✅ Maintain calorie deficit

✅ 30–45 min cardio daily

✅ Drink more water

✅ Sleep properly

Best exercises:
- Running
- Skipping
- Cycling
- HIIT workouts
"""

    # ---------- MUSCLE GAIN ---------- #

    elif (
        "muscle" in user_input
        or "bulk" in user_input
        or "gain muscle" in user_input
    ):

        return """
💪 MUSCLE GAIN PLAN

✅ High protein diet
(1.6–2g protein per kg body weight)

✅ Heavy strength training

✅ Eat in calorie surplus

✅ Sleep 7–8 hours

✅ Progressive overload is important

Best exercises:
- Bench Press
- Squats
- Deadlift
- Pull Ups
"""

    # ---------- ABS ---------- #

    elif "abs" in user_input or "core" in user_input:

        return """
🔥 ABS / CORE WORKOUT

Exercises:
- Plank (3 sets)
- Crunches (3 sets)
- Leg Raises (3 sets)
- Mountain Climbers
- Russian Twists

Tips:
✅ Maintain low body fat
✅ Do cardio regularly
✅ Avoid junk food
"""

    # ---------- DIET ---------- #

    elif "diet" in user_input or "meal" in user_input:

        return """
🥗 SIMPLE FITNESS DIET

🍳 Breakfast:
Eggs + banana + milk

🍚 Lunch:
Rice + chicken/dal + vegetables

🥜 Snacks:
Dry fruits + fruits

🍗 Dinner:
Light protein meal

❌ Avoid:
- Sugar
- Soft drinks
- Fried food
"""

    # ---------- CALORIES ---------- #

    elif "calories" in user_input or "calorie" in user_input:

        return """
🔥 CALORIES GUIDE

Calories are units of energy.

✅ Weight Loss:
Eat fewer calories than you burn.

✅ Muscle Gain:
Eat more calories than you burn.

✅ Maintenance:
Eat equal calories to maintain weight.

Focus on healthy calorie sources.
"""

    # ---------- WORKOUT ---------- #

    elif (
        "exercise" in user_input
        or "workout" in user_input
        or "training" in user_input
    ):

        return """
🏋 FITNESS WORKOUT GUIDE

Best beginner exercises:
- Pushups
- Squats
- Pull Ups
- Running
- Planks

Weekly plan:
✅ Strength training: 4–5 days
✅ Cardio: 3–4 days
✅ Rest: 1–2 days
"""

    # ---------- FITNESS TIPS ---------- #

    elif "fitness tips" in user_input or "tips" in user_input:

        return """
✨ FITNESS TIPS

✅ Stay consistent
✅ Drink enough water
✅ Sleep properly
✅ Eat balanced meals
✅ Track your progress
✅ Avoid junk food regularly
"""

    # ---------- DEFAULT ---------- #

    else:

        return """
🤖 AI FITNESS COACH

I can help you with:

🔥 Fat Loss
💪 Muscle Gain
🥗 Diet Plans
🏋 Workout Routines
📊 BMI
🔥 Calories
💯 Fitness Tips

Try asking:

- Best diet for fat loss
- How to gain muscle?
- What is BMI?
- Suggest abs workout
- Calories for weight loss
- Best beginner workout
"""