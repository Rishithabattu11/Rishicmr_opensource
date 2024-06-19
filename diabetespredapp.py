import os
import pickle
import streamlit as st

model_path=r"C:\Users\rishi\OneDrive\Desktop\cmr_opensource\diseaseprediction\diabetes_model.sav"
with open(model_path, 'rb') as f:
    diabetes_model = pickle.load(f)
# Set page configuration
st.set_page_config(page_title="Diabetes Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved diabetes model
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

# Page title
st.title('Diabetes Prediction using ML')

# Getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')

# Code for Prediction
diab_diagnosis = ''

# Creating a button for Prediction
if st.button('Diabetes Test Result'):
    user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                  BMI, DiabetesPedigreeFunction, Age]
    user_input = [float(x) for x in user_input]

    diab_prediction = diabetes_model.predict([user_input])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'

st.success(diab_diagnosis)
