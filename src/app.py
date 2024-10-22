import pickle
from flask import Flask, request, jsonify
import pandas as pd
import logging

# Initialize Flask app
app = Flask(__name__)

# Load the trained and tuned model (best_model.pkl)
def load_model(model_path='best_model.pkl'):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        logging.info("Model loaded successfully.")
        return model
    except FileNotFoundError:
        logging.error("Model file not found. Please check the path.")
        return None

# Function to preprocess incoming data for prediction
def preprocess_input(data):
    """
    Preprocess the input data (from JSON or form) before passing it to the model for prediction.
    Expected input: dictionary format, matching model feature names.
    """
    # Create DataFrame from input data
    df_input = pd.DataFrame(data, index=[0])
    logging.info(f"Input data received for prediction: {df_input}")
    
    # Return the DataFrame for prediction
    return df_input

# Load the best model at the start
model = load_model()

# Define a prediction route (API endpoint)
@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint for making predictions.
    Expected input: JSON or form with data corresponding to model features.
    """
    try:
        # Get data from the request (either form or JSON)
        input_data = request.get_json() if request.is_json else request.form.to_dict()
        
        # Preprocess the input data
        df_input = preprocess_input(input_data)
        
        # Make predictions using the loaded model
        prediction = model.predict(df_input)
        logging.info(f"Prediction made: {prediction[0]}")
        
        # Return the prediction as a JSON response
        return jsonify({
            'prediction': int(prediction[0])
        })
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Main entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
