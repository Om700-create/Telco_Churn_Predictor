# src/model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_model(X, y):
    """Train a Random Forest model and evaluate its performance."""
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the model
    model = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=None, min_samples_split=2)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    
    # Log the evaluation results
    print(f"Model Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(report)

    # Save the model
    joblib.dump(model, 'model.pkl')
    
    return model, report
