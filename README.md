# Telco Customer Churn Predictor

This project aims to predict customer churn for a telecommunications company using the Telco Customer Churn dataset from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). The project implements various machine learning models, such as Logistic Regression, Random Forest, and SVM, and includes model training, hyperparameter tuning, and API deployment.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Features](#features)
- [Usage](#usage)
- [API](#api)
- [Model Training](#model-training)
- [Model Deployment](#model-deployment)
- [Testing the API](#testing-the-api)
- [Contact](#contact)

## Project Overview
This project focuses on predicting whether a customer will churn based on several customer attributes such as contract type, monthly charges, and tenure. The project includes:
1. **Data Preprocessing**: Handling missing values and creating additional features.
2. **Feature Engineering**: Encoding categorical variables and scaling numeric features.
3. **Model Training**: Training Logistic Regression, Random Forest, and SVM models with hyperparameter tuning.
4. **Model Deployment**: Serving the model as an API for real-time predictions.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Om700-create/Telco_Churn_Predictor.git
    cd Telco_Churn_Predictor
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Dataset**:
    Download the dataset from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and place the `Telco-Customer-Churn.csv` file in the `data/` directory:
    ```
    data/telco_customer_churn.csv
    ```

## Dataset
The dataset contains information about a telecommunications company’s customers, including:
- **Demographic Information** (gender, SeniorCitizen, Partner, Dependents)
- **Services Subscribed** (phone service, multiple lines, internet service, online security, etc.)
- **Account Information** (contract type, payment method, monthly charges, total charges)

The target variable is `Churn`, which indicates whether the customer left within the last month.

## Features
Key features used in this project:
- **tenure**: Number of months the customer has stayed with the company.
- **MonthlyCharges**: The monthly charges the customer incurs.
- **TotalCharges**: The total amount charged to the customer.
- **Contract**: Type of contract (Month-to-month, One-year, Two-year).
- **InternetService**: Type of internet service (DSL, Fiber optic, No).
- **PaymentMethod**: How the customer pays (Electronic check, Mailed check, etc.).

## Usage

### 1. Data Preprocessing and Feature Engineering
To preprocess the data and perform feature engineering, run the following command:
```bash
python src/data_processing.py
This script will clean the dataset, handle missing values, and create new features. The processed data will be saved in the data/processed/ folder.

2. Training the Model
Train the model using different algorithms and perform hyperparameter tuning:

bash
Copy code
python src/model.py
The best model will be saved as best_model.pkl in the root directory.

3. Running the API
Deploy the model as a Flask API for real-time predictions:

bash
Copy code
python src/app.py
The API will be hosted at http://127.0.0.1:5000.

API
1. Endpoints
GET /: Returns a welcome message.
POST /predict: Accepts customer data as JSON and returns the churn prediction.
2. Example Input for POST /predict:
json
Copy code
{
    "tenure": 12,
    "MonthlyCharges": 70,
    "TotalCharges": 840,
    "gender_Male": 1,
    "Partner_Yes": 1,
    "Dependents_Yes": 0,
    "PhoneService_Yes": 1,
    "MultipleLines_No phone service": 0,
    "MultipleLines_Yes": 0,
    "InternetService_Fiber optic": 1,
    "InternetService_No": 0,
    "OnlineSecurity_Yes": 0,
    "TechSupport_Yes": 0,
    "Charges_per_Month": 70
}
3. Example Output:
json
Copy code
{
    "prediction": 0  # 0 means the customer is not likely to churn; 1 means the customer is likely to churn.
}
Model Training
This project uses Logistic Regression, Random Forest, and SVM for predicting churn. The models are tuned using GridSearchCV to find the best hyperparameters, and the best model is saved for deployment.

Model Deployment
Once the best model is trained, it is deployed using Flask, which serves predictions via an API. The API accepts JSON input and returns churn predictions based on the customer's data.

Testing the API
After running the Flask server, you can test the API using the test_prediction.py script:

bash
Copy code
python test_prediction.py
This script sends a POST request to the /predict endpoint with sample customer data and prints the churn prediction.

Contact
For any questions or issues, feel free to reach out:

GitHub: https://github.com/Om700-create/Telco_Churn_Predictor
Email: narayanbhandari498@gmail.com



