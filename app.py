import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model_lr.pkl", "rb"))

# Automatically get feature names in correct order
try:
    feature_names = list(model.feature_names_in_)
except:
    st.error("❌ The model file does not contain feature names info. Retrain the model with sklearn 1.0+")
    st.stop()

st.set_page_config(page_title="Possum Sex Predictor", page_icon="🦝", layout="wide")

st.markdown("<h1 style='text-align:center;'>🦝 Possum Sex Prediction Model</h1>", unsafe_allow_html=True)
st.write("Predict whether a possum is **Male or Female** based on biological measurements.")

# Sidebar Developer Info
st.sidebar.header("👤 Developer Info")
st.sidebar.markdown("**Name:** Sam Ingole")
st.sidebar.markdown("[🔗 LinkedIn](YOUR_LINKEDIN_LINK)")
st.sidebar.markdown("[💻 GitHub](YOUR_GITHUB_LINK)")
st.sidebar.markdown("📧 Email: your.email@example.com")
st.sidebar.write("---")

# UI
st.subheader("📥 Input Measurements")

col1, col2 = st.columns(2)

with col1:
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])
    hdlngth = st.number_input("Head Length", value=0.0)
    skullw = st.number_input("Skull Width", value=0.0)

with col2:
    totlngth = st.number_input("Total Length", value=0.0)
    taill = st.number_input("Tail Length", value=0.0)
    footlgth = st.number_input("Foot Length", value=0.0)

# Convert categorical Pop
Pop = 1 if Pop == "Vic" else 0

# Create dataframe in the SAME order as model was trained
input_data = pd.DataFrame([[Pop, hdlngth, skullw, totlngth, taill, footlgth]], columns=feature_names)

st.write("---")

if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    result = "🧑 Male" if prediction == 1 else "👩 Female"
    st.success(f"### 🎯 Predicted Sex: **{result}**")
