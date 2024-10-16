# src/data_processing.py
import pandas as pd

def load_data(filepath):
    """Load data from a CSV file."""
    df = pd.read_csv("C:/project/Telco_Churn_Predictor/data/telco_customer_churn.csv")
    return df

def preprocess_data(df):
    """Preprocess the DataFrame by cleaning and encoding categorical variables."""
    # Check for missing values and drop rows with any missing values
    if df.isnull().values.any():
        print("Missing values found. Dropping rows with missing values.")
        df = df.dropna()

    # Convert categorical columns to numeric using one-hot encoding
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    # Log the categorical columns being encoded
    print(f"Encoding categorical columns: {categorical_cols}")

    # Create dummies for categorical features
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df

