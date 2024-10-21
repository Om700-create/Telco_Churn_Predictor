import pandas as pd
from sklearn.preprocessing import RobustScaler

def load_processed_data(filepath):
    """
    Loads the processed Telco Customer Churn dataset from the specified CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Processed data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found at {filepath}. Please check the path.")
        return None

def add_charges_per_month(df):
    """
    Feature Engineering: Create 'Charges_per_Month' by dividing TotalCharges by tenure.
    Handle potential division by zero and missing values in 'TotalCharges'.
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=False)  # Replace NaNs with median (avoid inplace)
    df['Charges_per_Month'] = df['TotalCharges'] / df['tenure']
    df['Charges_per_Month'].fillna(0, inplace=False)  # Handle NaNs resulting from division by zero (avoid inplace)
    print("Feature 'Charges_per_Month' created.")
    return df

def feature_scaling(df, numerical_features):
    """
    Scale the numerical features using RobustScaler to handle potential outliers.
    """
    scaler = RobustScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    print(f"Scaled numerical features: {numerical_features}")
    return df

def feature_encoding(df, categorical_features):
    """
    Apply one-hot encoding to categorical features, including Tenure_Category (if it exists).
    """
    if 'Tenure_Category' in df.columns:
        df_encoded = pd.get_dummies(df, columns=categorical_features, drop_first=True)
    else:
        print("'Tenure_Category' column not found. Skipping encoding for this feature.")
        df_encoded = pd.get_dummies(df, columns=categorical_features[:-1], drop_first=True)  # Exclude Tenure_Category

    print(f"Encoded categorical features: {categorical_features if 'Tenure_Category' in df.columns else categorical_features[:-1]}")
    return df_encoded

def perform_feature_engineering(processed_data_path, final_data_path):
    """
    Perform full feature engineering on the dataset and save the final version to a CSV.
    """
    df = load_processed_data(processed_data_path)

    if df is None:
        return

    # Numerical and Categorical features to be processed
    numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Charges_per_Month']
    categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                            'InternetService', 'OnlineSecurity', 'TechSupport', 'Tenure_Category']  # Include 'Tenure_Category'

    # Feature Engineering steps
    df = add_charges_per_month(df)
    df = feature_scaling(df, numerical_features)
    df = feature_encoding(df, categorical_features)

    # Save the final engineered dataset
    df.to_csv(final_data_path, index=False)
    print(f"Feature engineered data saved to {final_data_path}")

# File paths
processed_data_path = "C:/project/Telco_Churn_Predictor/data/processed/telco_customer_churn_processed.csv"
final_data_path = "C:/project/Telco_Churn_Predictor/data/processed/telco_customer_churn_final.csv"

# Execute feature engineering
if __name__ == "__main__":
    perform_feature_engineering(processed_data_path, final_data_path)
