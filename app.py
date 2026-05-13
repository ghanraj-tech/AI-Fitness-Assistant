import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

from core.bmi import calculate_bmi, bmi_status
from core.calorie import calculate_calories
from core.predictor import predict_months

from plans.diet_plan import get_diet_plan
from plans.workout_plan import get_workout_plan

from modules.chatbot import get_fitness_response
from modules.pdf_report import generate_pdf


# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Fitness Assistant",
    page_icon="💪",
    layout="wide"
)


# ---------------- SESSION STATE ---------------- #
if "report_generated" not in st.session_state:
    st.session_state.report_generated = False

if "report_data" not in st.session_state:
    st.session_state.report_data = {}

if "chat_response" not in st.session_state:
    st.session_state.chat_response = ""


# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    selected = option_menu(
        menu_title="AI Fitness Assistant",
        options=["Home", "Fitness Report", "About"],
        icons=["house", "activity", "info-circle"],
        menu_icon="heart-pulse",
        default_index=0
    )


# ---------------- HOME PAGE ---------------- #
if selected == "Home":

    st.title("💪 AI Fitness Assistant")

    st.markdown("""
    ## Welcome to Your Smart Fitness Trainer

    Features:
    - BMI Analysis  
    - Calorie Calculation  
    - ML Weight Prediction  
    - Diet & Workout Plans  
    - Fitness Score  
    - PDF Report Generator  
    - AI Chatbot  
    """)


# ---------------- FITNESS REPORT PAGE ---------------- #
elif selected == "Fitness Report":

    st.title("📊 Personalized Fitness Report")

    # ---------------- INPUTS ---------------- #
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])

        age = st.number_input("Age", 10, 100, 20)

        height = st.number_input("Height (cm)", 100, 250, 170)

    with col2:
        current_weight = st.number_input("Current Weight (kg)", 30, 200, 80)

        target_weight = st.number_input("Target Weight (kg)", 30, 200, 70)

        activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])

    goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])


    # ---------------- GENERATE REPORT ---------------- #
    if st.button("Generate Report"):

        bmi = calculate_bmi(current_weight, height)
        bmi_result = bmi_status(bmi)

        calories = calculate_calories(
            gender, current_weight, height, age, activity
        )

        timeline = predict_months(current_weight, target_weight)

        diet = get_diet_plan(goal)
        workout = get_workout_plan(goal)

        # Fitness score
        score = 100
        if bmi > 25:
            score -= 20
        if activity == "Sedentary":
            score -= 15
        if current_weight > target_weight:
            score -= 10

        # STORE IN SESSION STATE (IMPORTANT FIX)
        st.session_state.report_generated = True

        st.session_state.report_data = {
            "BMI": bmi,
            "Status": bmi_result,
            "Calories Needed": calories,
            "Fitness Score": score,
            "Current Weight": current_weight,
            "Target Weight": target_weight,
            "Diet Plan": diet,
            "Workout Plan": workout,
            "Timeline": timeline
        }


    # ---------------- DISPLAY REPORT ---------------- #
    if st.session_state.report_generated:

        data = st.session_state.report_data

        st.subheader("📌 Fitness Metrics")

        c1, c2, c3 = st.columns(3)
        c1.metric("BMI", data["BMI"])
        c2.metric("Calories", f'{data["Calories Needed"]} kcal')
        c3.metric("Score", f'{data["Fitness Score"]}/100')

        st.success(f"Status: {data['Status']}")

        st.info(f"Timeline: {data['Timeline']} months")


        # ---------------- DIET & WORKOUT ---------------- #
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("🥗 Diet Plan")
            for item in data["Diet Plan"]:
                st.write("✅", item)

        with col4:
            st.subheader("🏋 Workout Plan")
            for item in data["Workout Plan"]:
                st.write("🏃", item)


        # ---------------- GRAPH ---------------- #
        st.subheader("📉 Weight Progress")

        fig, ax = plt.subplots()

        ax.plot(
            [0, data["Timeline"]],
            [data["Current Weight"], data["Target Weight"]],
            marker="o"
        )

        ax.set_xlabel("Months")
        ax.set_ylabel("Weight (kg)")

        st.pyplot(fig)


        # ---------------- PDF ---------------- #
        st.subheader("📄 Download Report")

        if st.button("Generate PDF"):

            file_path = generate_pdf(data)

            with open(file_path, "rb") as file:
                st.download_button(
                    "Download PDF",
                    file,
                    file_name="fitness_report.pdf",
                    mime="application/pdf"
                )


    # ---------------- CHATBOT ---------------- #
    st.markdown("---")
    st.header("🤖 AI Fitness Chatbot")

    user_question = st.text_input("Ask your question:", key="chat")

    if st.button("Ask AI"):
        if user_question.strip():
            st.session_state.chat_response = get_fitness_response(user_question)

    if st.session_state.chat_response:
        st.success(st.session_state.chat_response)


# ---------------- ABOUT PAGE ---------------- #
elif selected == "About":

    st.title("ℹ About")

    st.markdown("""
    AI Fitness Assistant Project:

    - Streamlit UI  
    - ML Prediction  
    - Diet & Workout Generator  
    - Chatbot  
    - PDF Reports  
    """)