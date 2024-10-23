from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Load the pre-trained model
model = joblib.load("C:/project/Telco_Churn_Predictor/best_model.pkl")

# Features used in the model
features = [
    'tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 'Partner_Yes',
    'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service',
    'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_Yes', 'TechSupport_Yes', 'Charges_per_Month'
]

@app.route('/')
def home():
    return "Welcome to the Telco Customer Churn Prediction API!"

# Predict function for the POST request
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        logging.info(f"Received data: {data}")
        
        # Convert the JSON data into a DataFrame (for easy compatibility with the model)
        df = pd.DataFrame([data], columns=features)
        
        # Perform the prediction using the loaded model
        prediction = model.predict(df)[0]
        
        # Return the prediction as a JSON response
        return jsonify({'prediction': int(prediction)})
    
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

