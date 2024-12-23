import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the encoder and model
with open(r"C:\Users\Ranjan kumar pradhan\.vscode\autism_prediction\encoders.pkl", "rb") as file:
    encoder = pickle.load(file)

with open(r"C:\Users\Ranjan kumar pradhan\.vscode\autism_prediction\best_model.pkl", "rb") as file:
    model = pickle.load(file)

# App Title
st.title("Autism Prediction API")
st.write("This app predicts the likelihood of Autism Spectrum Disorder (ASD) based on behavioral and demographic data.")

# Input Form
st.header("Enter the following details:")

# User Input Fields
A1_Score = st.selectbox("A1 Score", [1, 0], help="1 for yes, 0 for no")
A2_Score = st.selectbox("A2 Score", [1, 0])
A3_Score = st.selectbox("A3 Score", [1, 0])
A4_Score = st.selectbox("A4 Score", [1, 0])
A5_Score = st.selectbox("A5 Score", [1, 0])
A6_Score = st.selectbox("A6 Score", [1, 0])
A7_Score = st.selectbox("A7 Score", [1, 0])
A8_Score = st.selectbox("A8 Score", [1, 0])
A9_Score = st.selectbox("A9 Score", [1, 0])
A10_Score = st.selectbox("A10 Score", [1, 0])
gender = st.selectbox("Gender", ["f", "m"])
ethnicity = st.selectbox(
    "Ethnicity",
    ["?", "White-European", "Middle Eastern", "Pasifika", "Black", "Others", 
     "Hispanic", "Asian", "Turkish", "South Asian", "Latino", "others"]
)
jaundice = st.selectbox("Jaundice", ["no", "yes"])
austim = st.selectbox("Family History of Autism", ["no", "yes"])
contry_of_res = st.text_input("Country of Residence", "Enter your country")
used_app_before = st.selectbox("Used Screening App Before", ["no", "yes"])
age = st.slider("Age", 1, 100, 18)
relation = st.selectbox(
    "Relation to the Person",
    ["Self", "Relative", "Parent", "?", "Others", "Health care professional"]
)

# Prediction Logic
if st.button("Predict"):
    try:
        # Prepare the input data
        input_data = pd.DataFrame({
            "A1_Score": [A1_Score],
            "A2_Score": [A2_Score],
            "A3_Score": [A3_Score],
            "A4_Score": [A4_Score],
            "A5_Score": [A5_Score],
            "A6_Score": [A6_Score],
            "A7_Score": [A7_Score],
            "A8_Score": [A8_Score],
            "A9_Score": [A9_Score],
            "A10_Score": [A10_Score],
            "gender": [gender],
            "ethnicity": [ethnicity],
            "jaundice": [jaundice],
            "austim": [austim],
            "contry_of_res": [contry_of_res],
            "used_app_before": [used_app_before],
            "age": [age],
            "relation": [relation]
        })

        # Encode the input data
        input_data_encoded = encoder.transform(input_data)

        # Make the prediction
        prediction = model.predict(input_data_encoded)
        prediction_proba = model.predict_proba(input_data_encoded)

        # Display the result
        st.subheader("Prediction Results:")
        st.write("Prediction: ", "ASD Detected" if prediction[0] == 1 else "No ASD Detected")
        st.write(f"Confidence: {np.max(prediction_proba) * 100:.2f}%")

    except Exception as e:
        st.error(f"Error occurred: {e}")
