from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the saved model (assuming it's a Random Forest model)
model = joblib.load("best_random__model.pkl")  # Replace with the actual saved model filename

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to receive customer data and predict churn using the saved model.
    """
    try:
        # Get the customer data from the request
        data = request.get_json()

        # Check if data is present and in JSON format
        if not data:
            return jsonify({'error': 'No data provided in the request'}), 400

        # Convert the data to a pandas DataFrame
        df = pd.DataFrame([data])

        # Preprocess the data (e.g., one-hot encoding categorical features) as needed
        # ... (Your preprocessing logic might go here)

        # Make predictions using the loaded model
        predictions = model.predict(df)
        predicted_churn = predictions[0]  # Assuming single prediction

        # Prepare the response
        response = {
            'prediction': predicted_churn,
            'message': "Customer churn predicted successfully!"
        }

        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)