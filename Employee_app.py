import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ============================
# 🔹 Load Both Models
# ============================
@st.cache_data
def load_models():
    with open("final_burnout_model.pkl", "rb") as f1:
        burnout_model = pickle.load(f1)
    with open("final_productivity_model.pkl", "rb") as f2:
        productivity_model = pickle.load(f2)
    return burnout_model, productivity_model

burnout_model, productivity_model = load_models()

# ============================
# 🔹 Streamlit App Layout
# ============================
st.title("💼 Employee Analytics Dashboard")
st.write("Predict both **Burnout Risk** and **Productivity Level** using Machine Learning.")

# Tabs for each prediction
tab1, tab2 = st.tabs(["🔥 Burnout Prediction", "📈 Productivity Prediction"])

# ============================
# 🔹 TAB 1: Burnout Prediction
# ============================
with tab1:
    st.subheader("Predict Burnout Risk")

    # Input fields for burnout model
    gender = st.selectbox("Gender", ["Male", "Female"])
    company_type = st.selectbox("Company Type", ["Service", "Product"])
    wfh = st.selectbox("WFH Setup Available", ["Yes", "No"])
    hours = st.slider("Hours Worked Per Week", 30, 80, 45)
    overtime = st.slider("Overtime Hours", 0, 20, 5)
    tasks = st.number_input("Tasks Completed", 0, 100, 40)
    stress = st.slider("Stress Level (1-10)", 1.0, 10.0, 6.5)
    satisfaction = st.slider("Satisfaction Score (1-10)", 1.0, 10.0, 7.0)
    performance = st.slider("Performance Score", 0, 100, 75)
    absenteeism = st.number_input("Absenteeism Days", 0, 30, 2)
    burn_rate = st.slider("Burn Rate", 0.0, 1.0, 0.45)

    burnout_input = pd.DataFrame([{
        "Gender": gender,
        "Company_Type": company_type,
        "WFH_Setup_Available": wfh,
        "Hours_Worked_Per_Week": hours,
        "Overtime_Hours": overtime,
        "Tasks_Completed": tasks,
        "Stress_Level": stress,
        "Satisfaction_Score": satisfaction,
        "Performance_Score": performance,
        "Absenteeism_Days": absenteeism,
        "Burn_Rate": burn_rate
    }])

    if st.button("🔮 Predict Burnout Risk"):
        try:
            burnout_input = burnout_input.reindex(columns=burnout_model.feature_names_in_, fill_value=0)
            burnout_pred = burnout_model.predict(burnout_input)
            st.success(f"Predicted Burnout Risk: {burnout_pred[0]}")
        except Exception as e:
            st.error(f"Error: {e}")

# ============================
# 🔹 TAB 2: Productivity Prediction
# ============================
with tab2:
    st.subheader("Predict Productivity Level")

    # Input fields (same or slightly different)
    gender = st.selectbox("Gender", ["Male", "Female"], key="prod_gender")
    company_type = st.selectbox("Company Type", ["Service", "Product"], key="prod_company")
    wfh = st.selectbox("WFH Setup Available", ["Yes", "No"], key="prod_wfh")
    hours = st.slider("Hours Worked Per Week", 30, 80, 45, key="prod_hours")
    tasks = st.number_input("Tasks Completed", 0, 100, 40, key="prod_tasks")
    performance = st.slider("Performance Score", 0, 100, 75, key="prod_performance")
    satisfaction = st.slider("Satisfaction Score", 1.0, 10.0, 7.0, key="prod_satisfaction")
    stress = st.slider("Stress Level (1-10)", 1.0, 10.0, 6.5, key="prod_stress")

    prod_input = pd.DataFrame([{
        "Gender": gender,
        "Company_Type": company_type,
        "WFH_Setup_Available": wfh,
        "Hours_Worked_Per_Week": hours,
        "Tasks_Completed": tasks,
        "Performance_Score": performance,
        "Satisfaction_Score": satisfaction,
        "Stress_Level": stress
    }])

    if st.button("📊 Predict Productivity"):
        try:
            prod_input = prod_input.reindex(columns=productivity_model.feature_names_in_, fill_value=0)
            prod_pred = productivity_model.predict(prod_input)
            st.success(f"Predicted Productivity Level: {prod_pred[0]}")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Built by Amisha 🧠 — MSc Economics & Analytics")
