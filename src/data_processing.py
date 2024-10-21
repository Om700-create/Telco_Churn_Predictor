import pandas as pd
import numpy as np
import os

# File path to load the dataset
file_path = "C:/project/Telco_Churn_Predictor/data/telco_customer_churn.csv"
processed_data_dir = "C:/project/Telco_Churn_Predictor/data/processed"
processed_file_path = os.path.join(processed_data_dir, "telco_customer_churn_processed.csv")


def load_data(filepath):
    """
    Load the Telco Customer Churn dataset from the specified CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}. Please check the path.")
        return None


def handle_missing_values(df):
    """
    Handle missing values in the dataset. This function handles:
    1. Missing values in 'TotalCharges' by filling them with the median.
    """
    if df.isnull().sum().any():
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
        print("Handled missing values in 'TotalCharges'")
    else:
        print("No missing values found.")
    return df


def convert_data_types(df):
    """
    Convert data types for certain columns to ensure they are suitable for analysis.
    """
    # Convert SeniorCitizen to boolean for better analysis
    df['SeniorCitizen'] = df['SeniorCitizen'].astype(bool)
    print("Converted 'SeniorCitizen' to boolean.")
    
    # Convert other relevant columns if needed
    return df


def save_cleaned_data(df, save_path):
    """
    Save the cleaned dataset to the processed data directory.
    """
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    
    df.to_csv(save_path, index=False)
    print(f"Cleaned data saved to {save_path}")


def process_data(filepath, save_path):
    """
    Full data processing pipeline.
    1. Load the data.
    2. Handle missing values.
    3. Convert necessary data types.
    4. Save the cleaned dataset.
    """
    df = load_data(filepath)
    if df is not None:
        df = handle_missing_values(df)
        df = convert_data_types(df)
        save_cleaned_data(df, save_path)
        print("Data processing complete.")
    else:
        print("Data processing failed.")


if __name__ == "__main__":
    process_data(file_path, processed_file_path)




