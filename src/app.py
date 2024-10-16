# src/app.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("C:/project/Telco_Churn_Predictor/notebooks/best_random_forest_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    """Predict the churn based on the input features."""
    data = request.json
    df = pd.DataFrame(data)
    
    # Preprocess the data
    # You may need to adjust this based on your preprocessing steps
    df = df.drop(columns=['unnecessary_columns'], errors='ignore')  # Replace with actual columns to drop
    df = pd.get_dummies(df, drop_first=True)

    # Ensure the features match the training set
    missing_cols = set(model.feature_names_in_) - set(df.columns)
    for col in missing_cols:
        df[col] = 0
    df = df[model.feature_names_in_]

    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
