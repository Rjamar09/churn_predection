import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.sav', 'rb'))

# Define the input fields for the user interface
gender = st.selectbox('Gender', ['Female', 'Male'])
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
senior_citizen = st.selectbox('Senior Citizen', ['Yes', 'No'])
tenure = st.slider('Tenure (months)', 0, 72, 1)
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines = st.selectbox('Multiple Lines', ['No phone service', 'No', 'Yes'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['No', 'Yes', 'No internet service'])
online_backup = st.selectbox('Online Backup', ['No', 'Yes', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['No', 'Yes', 'No internet service'])
tech_support = st.selectbox('Tech Support', ['No', 'Yes', 'No internet service'])
streaming_tv = st.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'])
streaming_movies = st.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
monthly_charges = st.number_input('Monthly Charges ($)', value=0, step=1)
total_charges = st.number_input('Total Charges ($)', value=0, step=1)
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

# Convert the input data into a format the model can use
gender_bin = 1 if gender == 'Male' else 0
partner_bin = 1 if partner == 'Yes' else 0
dependents_bin = 1 if dependents == 'Yes' else 0
senior_citizen_bin = 1 if senior_citizen == 'Yes' else 0
phone_service_bin = 1 if phone_service == 'Yes' else 0
multiple_lines_bin = 1 if multiple_lines == 'Yes' else 2 if multiple_lines == 'No phone service' else 0
internet_service_bin = 1 if internet_service == 'Fiber optic' else 0 if internet_service == 'DSL' else -1
online_security_bin = 1 if online_security == 'Yes' else -1 if online_security == 'No internet service' else 0
online_backup_bin = 1 if online_backup == 'Yes' else -1 if online_backup == 'No internet service' else 0
device_protection_bin = 1 if device_protection == 'Yes' else -1 if device_protection == 'No internet service' else 0
paperless_billing_bin = 1 if paperless_billing == 'Yes' else 0
monthly_charges = monthly_charges

