# src/feature_engineering.py
import pandas as pd

def create_features(df):
    """Create new features for modeling."""
    
    # Check if required columns are in the DataFrame
    if 'TotalCharges' in df.columns and 'tenure' in df.columns:
        # Calculate charges per month
        df['Charges_per_Month'] = df['TotalCharges'] / df['tenure']
    else:
        print("Required columns not found for feature engineering.")

    # Check if 'Tenure_Category' exists and convert it to dummies
    if 'Tenure_Category' in df.columns:
        print("Creating dummy variables for 'Tenure_Category'.")
        tenure_dummies = pd.get_dummies(df['Tenure_Category'], prefix='Tenure', drop_first=True)
        df = pd.concat([df, tenure_dummies], axis=1)
        df.drop('Tenure_Category', axis=1, inplace=True)

    return df
