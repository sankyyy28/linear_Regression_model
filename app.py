import streamlit as st
import pandas as pd
import pickle

# Load Model and Scaler
model = pickle.load(open("model_lr.pkl", "rb"))
scaler = pickle.load(open("scaler_lr.pkl", "rb"))

# Feature list in the **same order used during training**
feature_names = ['Pop', 'head_l', 'skull_w', 'totlngth', 'footlgth', 'eye', 'chest', 'belly']

st.set_page_config(page_title="Possum Sex Predictor", page_icon="🦝", layout="wide")

st.markdown("<h1 style='text-align:center;'>🦝 Possum Sex Prediction Model</h1>", unsafe_allow_html=True)
st.write("Enter possum measurements to predict whether it is **Male or Female**.")

# Sidebar Developer Info
st.sidebar.header("👤 DATA SCIENTIST")
st.sidebar.markdown("**Name:** SANKET SANJAY SONPARATE")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/sanket-sonparate-018350260)")
st.sidebar.markdown("[💻 GitHub](https://github.com/sankyyy28)")
st.sidebar.markdown("📧 Email: your.sonparatesanket@gmail.com")
st.sidebar.write("---")

# Input Form
st.subheader("📥 Input Measurements")

col1, col2 = st.columns(2)

with col1:
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])
    head_l = st.number_input("Head Length")
    skull_w = st.number_input("Skull Width")
    totlngth = st.number_input("Total Length")

with col2:
    footlgth = st.number_input("Foot Length")
    eye = st.number_input("Eye Size")
    chest = st.number_input("Chest Size")
    belly = st.number_input("Belly Size")

# Encoding Pop
Pop = 1 if Pop == "Vic" else 0

# Create input DataFrame in the **correct column order**
input_data = pd.DataFrame([[Pop, head_l, skull_w, totlngth, footlgth, eye, chest, belly]], 
                          columns=feature_names)

# Prediction Button
st.write("---")
if st.button("🔍 Predict"):
    # Scale input
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)[0]
    result = "🧑 Male" if prediction == 1 else "👩 Female"

    st.success(f"### 🎯 Predicted Sex: **{result}**")

