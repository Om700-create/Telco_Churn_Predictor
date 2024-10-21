from src.data_processing import preprocess_data

# File path for the CSV file
filepath = "C:/project/Telco_Churn_Predictor/data/telco_customer_churn.csv"

# Run the preprocessing pipeline
df_preprocessed = preprocess_data(filepath)

# Display the first few rows of the processed data
if df_preprocessed is not None:
    print("Preprocessed Data:")
    print(df_preprocessed.head())
else:
    print("Data processing failed.")
