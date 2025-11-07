import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("model_lr.pkl", "rb"))

# Page Setup
st.set_page_config(page_title="Possum Sex Predictor", layout="wide")
st.title("🦝 Possum Sex Prediction App")

st.write("Enter possum biological measurements and predict if it's **Male or Female**.")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])
    head_l = st.number_input("Head Length", 0.0)
    skull_w = st.number_input("Skull Width", 0.0)
    totlngth = st.number_input("Total Length", 0.0)

with col2:
    footlgth = st.number_input("Foot Length", 0.0)
    eye = st.number_input("Eye Size", 0.0)
    chest = st.number_input("Chest Size", 0.0)
    belly = st.number_input("Belly Size", 0.0)

# Encode Pop
Pop = 1 if Pop == "Vic" else 0

# Prepare data for prediction
input_data = pd.DataFrame([[Pop, head_l, skull_w, totlngth, footlgth, eye, chest, belly]],
                          columns=["Pop", "h_l", "skull_w", "totlngth", "footlgth", "eye", "chest", "belly"])

# Predict Button
if st.button("🔍 Predict Sex"):
    prediction = model.predict(input_data)[0]
    result = "🧑 Male" if prediction == 1 else "👩 Female"
    st.success(f"### Predicted Sex: **{result}**")

# Sidebar Developer Info
with st.sidebar:
    st.header("👤 Developer Info")
    st.markdown("**Name:** SANKET S. SONPARATE")

    st.markdown("[🔗 LinkedIn](YOUR_LINKEDIN_URL)")
    st.markdown("[💻 GitHub](YOUR_GITHUB_URL)")
    st.markdown("📧 sonparatesanket@gmail.com")
