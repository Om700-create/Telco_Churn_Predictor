from flask import Flask, request, jsonify
import pandas as pd
import logging
from utils import load_model, validate_input, log_error_and_format

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Load the pre-trained model using the utility function
model_path = "C:/project/Telco_Churn_Predictor/best_model.pkl"
model = load_model(model_path)

# Features used in the model
features = [
    'tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 'Partner_Yes',
    'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service',
    'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No',
    'OnlineSecurity_Yes', 'TechSupport_Yes', 'Charges_per_Month',
    'Contract_One year', 'Contract_Two year', 'DeviceProtection_No internet service',
    'DeviceProtection_Yes', 'OnlineBackup_No internet service', 'OnlineBackup_Yes',
    'PaperlessBilling_Yes', 'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
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
        
        # Validate the input using the utility function
        validation_error = validate_input(data, features)
        if validation_error:
            return jsonify({'error': validation_error}), 400
        
        # Convert the JSON data into a DataFrame (for easy compatibility with the model)
        df = pd.DataFrame([data], columns=features)
        
        # Perform the prediction using the loaded model
        prediction = model.predict(df)[0]
        
        # Return the prediction as a JSON response
        return jsonify({'prediction': int(prediction)})
    
    except Exception as e:
        # Log the error using the utility function
        return jsonify(log_error_and_format("Error during prediction", e)), 500

if __name__ == '__main__':
    app.run(debug=True)

