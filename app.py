import streamlit as st
import pandas as pd
import numpy as np
from pickle import load

# Carga del modelo
model = load(open("maternal-risk-model.pkl","rb"))

# Título de la app
st.title("Predicción de Riesgo Materno")

# Inputs del usuario
age = st.number_input("Edad de la madre", 15, 50)
systolic_bp = st.slider("Presión sistólica", 80, 200)
diastolic_bp = st.slider("Presión diastólica", 40, 150)
blood_sugar = st.slider("Nivel de azúcar en sangre (mg/dL)", 50, 300)
body_temp = st.slider("Temperatura corporal (°C)", 35.0, 42.0)
heart_rate = st.slider("Frecuencia cardíaca (lpm)", 40, 180)

# Botón de predicción
if st.button("Predecir Riesgo"):
    input_data = np.array([[age, systolic_bp, diastolic_bp, blood_sugar, body_temp, heart_rate]])
    prediction = model.predict(input_data)[0]
    
    st.write(f"**Nivel de riesgo materno predicho:** {prediction}")
