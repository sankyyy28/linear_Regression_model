import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model_lr.pkl", "rb"))

# Feature list (same order as training)
feature_names = ['Pop', 'hdlngth', 'skullw', 'totlngth', 'taill', 'footlgth']

st.set_page_config(page_title="Possum Sex Predictor", page_icon="🦝", layout="wide")

st.markdown("<h1 style='text-align:center;'>🦝 Possum Sex Prediction Model</h1>", unsafe_allow_html=True)
st.write("Predict whether a possum is **Male or Female** based on measurements.")

# Sidebar Developer Info
st.sidebar.header("👤 Developer Info")
st.sidebar.markdown("**Name:** Sam Ingole")
st.sidebar.markdown("[🔗 LinkedIn](YOUR_LINKEDIN_LINK)")
st.sidebar.markdown("[💻 GitHub](YOUR_GITHUB_LINK)")
st.sidebar.markdown("📧 Email: your.email@example.com")
st.sidebar.write("---")

# Input UI
st.subheader("📥 Input Measurements")

col1, col2 = st.columns(2)

with col1:
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])
    hdlngth = st.number_input("Head Length", value=0.0)
    skullw = st.number_input("Skull Width", value=0.0)
    

with col2:
    totlngth = st.number_input("Total Length", value=0.0)
    taill = st.number_input("Taill Length", value=0.0)
    footlgth = st.number_input("Foot Length", value=0.0)


# Convert Pop to numeric
Pop = 1 if Pop == "Vic" else 0

# Construct Input DataFrame
input_data = pd.DataFrame([[Pop, hdlngth, skullw, totlngth, taill, footlgth]],
                          columns=feature_names)

# Predict
st.write("---")
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    result = "🧑 Male" if prediction == 1 else "👩 Female"
    st.success(f"### 🎯 Predicted Sex: **{result}**")
