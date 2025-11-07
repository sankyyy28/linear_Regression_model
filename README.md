#  Possum Sex Prediction App

A Streamlit web application that predicts the sex of possums based on biological measurements using a trained machine learning model.

##  Project Overview

This application uses a **Linear Regression model** (`model_lr.pkl`) to predict whether a possum is male or female based on 12 different biological features. The model analyzes physical measurements and outputs a prediction with detailed decision factors.

##  Features

- **User-friendly Interface**: Clean, intuitive input forms for all biological measurements
- **Real-time Predictions**: Instant sex prediction based on input parameters
- **Decision Transparency**: Shows how each feature contributes to the final prediction
- **Sample Data**: Pre-loaded sample inputs for quick testing
- **Model Insights**: Displays model coefficients and feature importance
- **Responsive Design**: Works seamlessly on desktop and mobile devices

##  Technical Details

### Model Information
- **Algorithm**: Linear Regression
- **Input Features**: 12 biological measurements
- **Output**: Binary classification (Male/Female)
- **Threshold**: ≥0.5 = Male, <0.5 = Female

### Required Features
The model expects the following 12 features in exact order:

1. **case** - Case ID
2. **site** - Site location
3. **Pop** - Population (Vic/other)
4. **hdlngth** - Head Length
5. **skullw** - Skull Width
6. **totlngth** - Total Length
7. **taill** - Tail Length
8. **footlgth** - Foot Length
9. **earconch** - Ear Conch
10. **eye** - Eye measurement
11. **chest** - Chest measurement
12. **belly** - Belly measurement

##  Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step-by-Step Setup

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd possum-sex-predictor
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install streamlit pandas scikit-learn numpy
   ```

4. **Download Model File**
   - Ensure `model_lr.pkl` is in the same directory as the script

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

##  Usage Guide

### Basic Usage
1. **Open the application** in your web browser
2. **Fill in the measurements**:
   - Case ID and Site (numeric identifiers)
   - Population (select Vic or other)
   - Biological measurements (head length, skull width, etc.)
3. **Click "Predict Sex"** to get the prediction
4. **Review results** including confidence and decision factors

### Using Sample Data
- Click **"Load Sample Male"** or **"Load Sample Female"** in the sidebar
- These buttons pre-fill the form with realistic measurement values
- Useful for testing and understanding the model behavior

### Interpreting Results
- **🧑 Male**: Prediction score ≥ 0.5
- **👩 Female**: Prediction score < 0.5
- **Decision Factors**: Shows how each feature contributed to the prediction
- **Raw Score**: The actual numeric output from the model

##  Model Performance

The Linear Regression model provides:
- **Binary classification** based on a 0.5 threshold
- **Feature coefficients** indicating importance of each measurement
- **Transparent decision process** with contribution analysis

## 🔧 File Structure

```
possum-sex-predictor/
│
├── app.py                 # Main Streamlit application
├── model_lr.pkl          # Trained machine learning model
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

##  Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
pandas>=1.5.0
scikit-learn>=1.0.0
numpy>=1.21.0
```

##  Developer Information

**Developer**: Sanket Sanjay Sonparate 
**Email**: sonparatesanket@gmail.com  
**LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/sanket-sonparate-018350260)  
**GitHub**: [Your GitHub Profile](https://github.com/sankyyy28)  

##  Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Ensure `model_lr.pkl` is in the correct directory
   - Check file permissions

2. **Missing Dependencies**
   - Run `pip install -r requirements.txt`
   - Ensure compatible Python version

3. **Feature Mismatch**
   - The model expects exactly 12 features in specific order
   - Verify `model.feature_names_in_` matches input structure

4. **Prediction Errors**
   - Check for invalid input values
   - Ensure all numeric fields are filled

### Getting Help

If you encounter issues:
1. Check the error messages in the Streamlit interface
2. Verify all input values are within reasonable ranges
3. Ensure the model file hasn't been corrupted
4. Contact the developer with error details

## 🔮 Future Enhancements

Potential improvements for the application:
- [ ] Add model performance metrics
- [ ] Include data visualization charts
- [ ] Add batch prediction capability
- [ ] Implement user authentication
- [ ] Add export functionality for results
- [ ] Include model retraining interface

##  License

This project is for educational and demonstration purposes. Please ensure proper attribution when using or modifying the code.

##  Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---
