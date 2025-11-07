import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
try:
    model = pickle.load(open("model_lr.pkl", "rb"))
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Automatically get feature names in correct order
try:
    feature_names = list(model.feature_names_in_)
    st.sidebar.info(f"Model expects {len(feature_names)} features: {', '.join(feature_names)}")
except:
    st.error("❌ The model file does not contain feature names info. Retrain the model with sklearn 1.0+")
    st.stop()

st.set_page_config(page_title="Possum Sex Predictor", page_icon="🦝", layout="wide")

st.markdown("<h1 style='text-align:center;'>🦝 Possum Sex Prediction Model</h1>", unsafe_allow_html=True)
st.write("Predict whether a possum is **Male or Female** based on biological measurements.")

# Sidebar Developer Info
st.sidebar.header("👤 Developer Info")
st.sidebar.markdown("**Name:** Sam Ingole")
st.sidebar.markdown("[🔗 LinkedIn](https://linkedin.com/in/sam-ingole)")
st.sidebar.markdown("[💻 GitHub](https://github.com/samingole)")
st.sidebar.markdown("📧 Email: sam.ingole@example.com")
st.sidebar.write("---")

# Display model info
st.sidebar.header("🔧 Model Info")
st.sidebar.write(f"Features: {len(feature_names)}")
st.sidebar.write(f"Intercept: {model.intercept_:.4f}")
st.sidebar.write("Coefficients:")
for feat, coef in zip(feature_names, model.coef_):
    st.sidebar.write(f"  {feat}: {coef:.4f}")

# UI - Collect all features from the model
st.subheader("📥 Input Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    case = st.number_input("Case ID", min_value=1, value=1)
    site = st.number_input("Site", min_value=1, value=1)
    Pop = st.selectbox("Population (Pop)", ["Vic", "other"])
    hdlngth = st.number_input("Head Length (hdlngth)", value=90.0, min_value=0.0, format="%.1f")
    skullw = st.number_input("Skull Width (skullw)", value=60.0, min_value=0.0, format="%.1f")

with col2:
    totlngth = st.number_input("Total Length (totlngth)", value=80.0, min_value=0.0, format="%.1f")
    taill = st.number_input("Tail Length (taill)", value=35.0, min_value=0.0, format="%.1f")
    footlgth = st.number_input("Foot Length (footlgth)", value=70.0, min_value=0.0, format="%.1f")
    earconch = st.number_input("Ear Conch (earconch)", value=50.0, min_value=0.0, format="%.1f")

with col3:
    eye = st.number_input("Eye (eye)", value=15.0, min_value=0.0, format="%.1f")
    chest = st.number_input("Chest (chest)", value=25.0, min_value=0.0, format="%.1f")
    belly = st.number_input("Belly (belly)", value=30.0, min_value=0.0, format="%.1f")

# Convert categorical Pop to numeric
Pop_numeric = 1 if Pop == "Vic" else 0

# Create dataframe in the EXACT same order as model was trained
input_data = pd.DataFrame([[
    case, site, Pop_numeric, hdlngth, skullw, totlngth, 
    taill, footlgth, earconch, eye, chest, belly
]], columns=feature_names)

# Display the input data for verification
st.write("---")
st.subheader("📋 Input Data Summary")
st.dataframe(input_data.T.rename(columns={0: "Value"}))

st.write("---")

if st.button("🔍 Predict Sex", type="primary"):
    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0] if hasattr(model, 'predict_proba') else None
        
        result = "🧑 Male" if prediction == 1 else "👩 Female"
        
        st.success(f"### 🎯 Predicted Sex: **{result}**")
        
        if probability is not None:
            st.info(f"### 📊 Prediction Confidence: **{max(probability)*100:.1f}%**")
            
        # Show decision factors
        st.subheader("🔍 Decision Factors")
        decision_score = model.intercept_
        factors_data = []
        
        for feat, coef, value in zip(feature_names, model.coef_, input_data.iloc[0]):
            contribution = coef * value
            decision_score += contribution
            factors_data.append({
                "Feature": feat,
                "Value": value,
                "Coefficient": coef,
                "Contribution": contribution
            })
        
        factors_df = pd.DataFrame(factors_data)
        st.dataframe(factors_df.style.format({
            "Value": "{:.2f}",
            "Coefficient": "{:.4f}",
            "Contribution": "{:.4f}"
        }))
        
        st.write(f"**Raw Decision Score**: {decision_score:.4f}")
        st.write(f"**Threshold**: 0.5")
        st.write(f"**Final Prediction**: {'Male' if decision_score >= 0.5 else 'Female'}")
        
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
        st.info("💡 Make sure all input values are within reasonable ranges.")

# Add some sample data for testing
st.sidebar.header("🧪 Sample Inputs")
if st.sidebar.button("Load Sample Male"):
    st.session_state.case = 1
    st.session_state.site = 1
    st.session_state.Pop = "Vic"
    st.session_state.hdlngth = 94.1
    st.session_state.skullw = 60.4
    st.session_state.totlngth = 89.0
    st.session_state.taill = 36.0
    st.session_state.footlgth = 74.5
    st.session_state.earconch = 51.2
    st.session_state.eye = 15.2
    st.session_state.chest = 28.0
    st.session_state.belly = 36.0

if st.sidebar.button("Load Sample Female"):
    st.session_state.case = 2
    st.session_state.site = 1
    st.session_state.Pop = "other"
    st.session_state.hdlngth = 92.5
    st.session_state.skullw = 57.6
    st.session_state.totlngth = 91.5
    st.session_state.taill = 36.5
    st.session_state.footlgth = 72.5
    st.session_state.earconch = 51.8
    st.session_state.eye = 16.0
    st.session_state.chest = 28.7
    st.session_state.belly = 33.7

st.sidebar.info("💡 Click the buttons above to load sample data for testing.")
