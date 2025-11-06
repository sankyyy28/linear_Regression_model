import streamlit as st
import pandas as pd
import pickle

# ==================== LOAD MODEL & SCALER ====================
model = pickle.load(open("model_lr.pkl", "rb"))
scaler = pickle.load(open("scaler_lr.pkl", "rb"))

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Possum Sex Prediction",
    page_icon="🦝",
    layout="wide"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #0E76A8, #104E8B);
        padding: 12px 25px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 18px;
    }
    .prediction-box {
        padding: 25px;
        border-radius: 12px;
        background-color: #F7F9FC;
        border: 2px solid #E5E7EB;
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
st.markdown('<div class="main-header">🦝 Possum Sex Prediction Model</div>', unsafe_allow_html=True)
st.write("Enter possum biological measurements and predict whether it's **Male or Female**.")


# ==================== SIDEBAR ====================
st.sidebar.header("👤 DATA SCIENTIST  ")
st.sidebar.markdown("**Name:** SANKET SANJAY SONPARATE")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/sanket-sonparate-018350260)")
st.sidebar.markdown("💻 [GitHub](https://github.com/sankyyy28)")
st.sidebar.markdown("📧 **Email:** sonparatesanketgmail.com")
st.sidebar.write("---")
st.sidebar.write("Developed with ❤️ using Streamlit.")


# ==================== INPUT FORM ====================
st.subheader("📥 Input Measurements")

col1, col2 = st.columns(2)

with col1:
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])
    head_l = st.number_input("Head Length", min_value=0.0)
    skull_w = st.number_input("Skull Width", min_value=0.0)
    totlngth = st.number_input("Total Length", min_value=0.0)

with col2:
    footlgth = st.number_input("Foot Length", min_value=0.0)
    eye = st.number_input("Eye Size", min_value=0.0)
    chest = st.number_input("Chest Size", min_value=0.0)
    belly = st.number_input("Belly Size", min_value=0.0)

# Encode Pop
Pop = 1 if Pop == "Vic" else 0

# Convert input to DataFrame
input_data = pd.DataFrame([[Pop, head_l, skull_w, totlngth, footlgth, eye, chest, belly]],
                          columns=['Pop', 'head_l', 'skull_w', 'totlngth', 'footlgth', 'eye', 'chest', 'belly'])

input_scaled = scaler.transform(input_data)


# ==================== PREDICTION ====================
st.write("---")
st.subheader("🎯 Prediction Result")

predict_col, blank = st.columns([1.5, 1])

with predict_col:
    if st.button("🔍 Predict Possum Sex", use_container_width=True):
        prediction = model.predict(input_scaled)[0]
        result = "🧑 Male" if prediction == 1 else "👩 Female"

        st.markdown(f"""
        <div class="prediction-box">
            <h3 style='text-align:center;'>Prediction Output</h3>
            <h1 style='text-align:center;'>{result}</h1>
        </div>
        """, unsafe_allow_html=True)
