import requests
import json

# URL for the prediction endpoint
url = 'http://127.0.0.1:5000/predict'

# Sample input data for prediction
data = {
    "tenure": 12,
    "MonthlyCharges": 70,
    "TotalCharges": 840,
    "gender_Male": 1,
    "Partner_Yes": 1,
    "Dependents_Yes": 0,
    "PhoneService_Yes": 1,
    "MultipleLines_No phone service": 0,
    "MultipleLines_Yes": 0,
    "InternetService_Fiber optic": 1,
    "InternetService_No": 0,
    "OnlineSecurity_Yes": 0,
    "TechSupport_Yes": 0,
    "Charges_per_Month": 70,
    "Contract_One year": 0,
    "Contract_Two year": 0,
    "DeviceProtection_No internet service": 0,
    "DeviceProtection_Yes": 0,
    "OnlineBackup_No internet service": 0,
    "OnlineBackup_Yes": 0,
    "PaperlessBilling_Yes": 1,
    "PaymentMethod_Credit card (automatic)": 0,
    "PaymentMethod_Electronic check": 1,
    "PaymentMethod_Mailed check": 0
}

# Sending the POST request to the API
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

# Output the API response
print(response.json())
