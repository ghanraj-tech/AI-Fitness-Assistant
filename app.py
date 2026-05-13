import streamlit as st
import matplotlib.pyplot as plt

from streamlit_option_menu import option_menu

from core.bmi import calculate_bmi, bmi_status
from core.calorie import calculate_calories
from core.predictor import predict_months

from plans.diet_plan import get_diet_plan
from plans.workout_plan import get_workout_plan


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Fitness Assistant",
    page_icon="💪",
    layout="wide"
)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    selected = option_menu(
        menu_title="AI Fitness Assistant",
        options=[
            "Home",
            "Fitness Report",
            "About"
        ],
        icons=[
            "house",
            "activity",
            "info-circle"
        ],
        menu_icon="heart-pulse",
        default_index=0
    )


# ---------------- HOME PAGE ---------------- #

if selected == "Home":

    st.title("💪 AI Fitness Assistant")

    st.markdown("""
    ## Welcome to Your Smart Fitness Trainer

    This AI-based application helps you with:

    ✅ BMI Analysis  
    ✅ Daily Calorie Calculation  
    ✅ Weight Prediction using ML  
    ✅ Personalized Workout Plans  
    ✅ Personalized Diet Plans  
    ✅ Fitness Score Analysis  
    ✅ Progress Visualization  

    ---
    """)

    st.info("Use the sidebar to generate your fitness report.")


# ---------------- FITNESS REPORT ---------------- #

if selected == "Fitness Report":

    st.title("📊 Personalized Fitness Report")


    # ---------- INPUTS ---------- #

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Select Gender",
            ["Male", "Female"]
        )

        age = st.number_input(
            "Enter Age",
            min_value=10,
            max_value=100,
            value=20
        )

        height = st.number_input(
            "Enter Height (cm)",
            min_value=100,
            max_value=250,
            value=170
        )

    with col2:

        current_weight = st.number_input(
            "Current Weight (kg)",
            min_value=30,
            max_value=200,
            value=80
        )

        target_weight = st.number_input(
            "Target Weight (kg)",
            min_value=30,
            max_value=200,
            value=70
        )

        activity = st.selectbox(
            "Activity Level",
            [
                "Sedentary",
                "Light",
                "Moderate",
                "Active"
            ]
        )


    goal = st.selectbox(
        "Select Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Maintenance"
        ]
    )


    # ---------- BUTTON ---------- #

    if st.button("Generate Report"):


        # ---------- CALCULATIONS ---------- #

        bmi = calculate_bmi(
            current_weight,
            height
        )

        bmi_result = bmi_status(bmi)

        calories = calculate_calories(
            gender,
            current_weight,
            height,
            age,
            activity
        )

        timeline = predict_months(
            current_weight,
            target_weight
        )

        diet = get_diet_plan(goal)

        workout = get_workout_plan(goal)


        # ---------- FITNESS SCORE ---------- #

        score = 100

        if bmi > 25:
            score -= 20

        if activity == "Sedentary":
            score -= 15

        if current_weight > target_weight:
            score -= 10


        # ---------- METRICS ---------- #

        st.subheader("📌 Fitness Metrics")

        m1, m2, m3 = st.columns(3)

        m1.metric("BMI", bmi)

        m2.metric("Calories", f"{calories} kcal")

        m3.metric("Fitness Score", f"{score}/100")


        # ---------- BMI STATUS ---------- #

        st.subheader("📊 BMI Status")

        st.success(f"Your BMI Status: {bmi_result}")


        # ---------- TIMELINE ---------- #

        st.subheader("🎯 Estimated Timeline")

        st.info(
            f"Approx {timeline} months required to reach your target weight."
        )


        # ---------- DIET & WORKOUT ---------- #

        col3, col4 = st.columns(2)

        with col3:

            st.subheader("🥗 Diet Plan")

            for item in diet:

                st.write(f"✅ {item}")

        with col4:

            st.subheader("🏋 Workout Plan")

            for exercise in workout:

                st.write(f"🏃 {exercise}")


        # ---------- FITNESS SCORE ---------- #

        st.subheader("💯 Fitness Score")

        st.progress(score / 100)


        # ---------- GRAPH ---------- #

        st.subheader("📉 Weight Progress Prediction")

        weights = [
            current_weight,
            target_weight
        ]

        months_data = [
            0,
            timeline
        ]

        fig, ax = plt.subplots()

        ax.plot(
            months_data,
            weights,
            marker='o'
        )

        ax.set_xlabel("Months")

        ax.set_ylabel("Weight (kg)")

        ax.set_title("Predicted Weight Journey")

        st.pyplot(fig)


# ---------------- ABOUT PAGE ---------------- #

if selected == "About":

    st.title("ℹ About Project")

    st.markdown("""
    ## AI Fitness Assistant

    This project is developed using:

    - Python
    - Streamlit
    - Machine Learning
    - Linear Regression
    - Matplotlib

    ### Features

    - Smart BMI Analysis
    - AI Weight Prediction
    - Personalized Recommendations
    - Fitness Visualization Dashboard

    ---
    Developed as an AI + ML Fitness Project.
    """)