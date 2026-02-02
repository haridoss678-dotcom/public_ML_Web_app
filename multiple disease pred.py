# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:43:17 2026

@author: Harid
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Harid/OneDrive/Documents/Multiple disease prediction/train model/trained_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/Harid/OneDrive/Documents/Multiple disease prediction/train model/heart_model.sav','rb'))

calories_pred_model = pickle.load(open('C:/Users/Harid/OneDrive/Documents/Multiple disease prediction/train model/calorie_model.sav','rb'))

# sidebar for navigate

with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Calories Burn Prediction"],
        icons=["activity", "heart", "fire"],
        default_index=0
    )


# =====================================================
# ================= DIABETES PAGE =====================
# =====================================================
if selected == "Diabetes Prediction":

    st.title("🩺 Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input("Pregnancies")

    with col2:
        glucose = st.text_input("Glucose")

    with col3:
        bp = st.text_input("Blood Pressure")

    with col1:
        skin = st.text_input("Skin Thickness")

    with col2:
        insulin = st.text_input("Insulin")

    with col3:
        bmi = st.text_input("BMI")

    with col1:
        dpf = st.text_input("DPF")

    with col2:
        age = st.text_input("Age")

    if st.button("Predict Diabetes"):

        data = [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]

        if "" in data:
            st.warning("Enter all values")
        else:
            pred = diabetes_model.predict([list(map(float, data))])[0]

            if pred == 1:
                st.error("🔴 Person HAS Diabetes")
            else:
                st.success("🟢 Person has NO Diabetes")


# =====================================================
# ================= HEART PAGE ========================
 

elif selected == "Heart Disease Prediction":

    st.title("❤️ Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    # -------- Row 1 --------
    with col1:
        age = st.text_input("Age")

    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])
        sex = 1 if sex == "Male" else 0

    with col3:
        cp = st.text_input("Chest Pain Type (cp)")


    # -------- Row 2 --------
    with col1:
        trestbps = st.text_input("Resting BP (trestbps)")

    with col2:
        chol = st.text_input("Cholesterol (chol)")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar (fbs)")


    # -------- Row 3 --------
    with col1:
        restecg = st.text_input("Rest ECG (restecg)")

    with col2:
        thalach = st.text_input("Max Heart Rate (thalach)")

    with col3:
        exang = st.text_input("Exercise Angina (exang)")


    # -------- Row 4 --------
    with col1:
        oldpeak = st.text_input("Oldpeak")

    with col2:
        slope = st.text_input("Slope")

    with col3:
        ca = st.text_input("CA (vessels)")


    # -------- Row 5 --------
    with col1:
        thal = st.text_input("Thal")


    # -------- Prediction --------
    if st.button("Predict Heart Disease"):

        inputs = [age, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal]

        if "" in inputs:
            st.warning("⚠ Please enter all values")

        else:
            features = [
                float(age),
                sex,
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]

            pred = heart_disease_model.predict([features])[0]

            if pred == 1:
                st.error("🔴 Person HAS Heart Disease")
            else:
                st.success("🟢 Person has NO Heart Disease")

# =====================================================
# ================= CALORIES PAGE =====================
# =====================================================
elif selected == "Calories Burn Prediction":

    st.title("🔥 Calories Burn Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        gender = 0 if gender == "Male" else 1

    with col2:
        age = st.text_input("Age")

    with col3:
        height = st.text_input("Height")

    with col1:
        weight = st.text_input("Weight")

    with col2:
        duration = st.text_input("Duration")

    with col3:
        heart_rate = st.text_input("Heart Rate")

    with col1:
        body_temp = st.text_input("Body Temp")


    # ✅ EVERYTHING INSIDE BUTTON
    if st.button("Predict Calories"):

        if "" in [age, height, weight, duration, heart_rate, body_temp]:
            st.warning("Enter all values")

        else:
            features = [
                gender,
                float(age),
                float(height),
                float(weight),
                float(duration),
                float(heart_rate),
                float(body_temp)
            ]

            calories = calories_pred_model.predict([features])[0]

            st.success(f"🔥 Calories Burned: {calories:.2f} kcal")