# Telco Customer Churn Predictor

This project aims to predict customer churn for a telecommunications company using the Telco Customer Churn dataset from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn). The project implements various machine learning models, such as Logistic Regression, Random Forest, and SVM, and includes model training, hyperparameter tuning, and API deployment. Additionally, the project includes a comprehensive **data analysis** phase to uncover insights and patterns in the dataset, which helps in understanding the factors influencing customer churn.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Data Analysis](#data-analysis)
- [Features](#features)
- [Usage](#usage)
- [API](#api)
- [Model Training](#model-training)
- [Model Deployment](#model-deployment)
- [Testing the API](#testing-the-api)
- [Contact](#contact)

## Project Overview
This project focuses on predicting whether a customer will churn based on several customer attributes such as contract type, monthly charges, and tenure. The project includes:
1. **Data Analysis**: Exploratory data analysis (EDA) to uncover patterns and insights related to customer churn.
2. **Data Preprocessing**: Handling missing values and creating additional features.
3. **Feature Engineering**: Encoding categorical variables and scaling numeric features.
4. **Model Training**: Training Logistic Regression, Random Forest, and SVM models with hyperparameter tuning.
5. **Model Deployment**: Serving the model as an API for real-time predictions.

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

## Data Analysis
The **data analysis** phase of this project involved a deep dive into the dataset to uncover patterns and insights related to customer churn. Below are some key findings from the analysis:

1. **Churn Rate**: 
   - **26.58%** of customers churned, while **73.42%** did not. This indicates an imbalanced dataset, which is common in churn prediction problems.

2. **Demographics and Churn**:
   - **Senior citizens** have a higher churn rate compared to non-senior citizens.
   - Customers **without partners** are more likely to churn than those with partners.
   - **Gender** does not significantly impact churn.

3. **Contract Type**:
   - **Month-to-month contracts** have the highest churn rate (**42.71%**), while **two-year contracts** have the lowest (**2.85%**).
   - Longer contract terms significantly reduce churn.

4. **Payment Methods**:
   - Customers using **electronic checks** have the highest churn rate (**45.29%**), while those using **automatic payment methods** (bank transfer or credit card) have the lowest (**16.73%** and **15.25%** respectively).

5. **Internet Service**:
   - **Fiber optic users** have the highest churn rate (**41.89%**), while **DSL users** have a much lower churn rate (**19.00%**).
   - Customers **without internet service** have the lowest churn rate (**7.43%**).

6. **Tenure**:
   - **New customers (0-12 months)** have the highest churn rate (**47.68%**), while long-term customers (**61+ months**) have the lowest (**6.61%**).
   - Improving the early customer experience could help reduce churn.

7. **Monthly and Total Charges**:
   - Churned customers pay **higher average monthly charges ($74.44)** compared to non-churned customers ($61.31).
   - **Total charges** for churned customers are significantly lower ($1,531.80) compared to retained customers ($2,555.34), indicating the impact of tenure on churn.

These insights were used to guide feature engineering and model training, ensuring that the predictive models are well-informed by real-world data patterns.

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
Copy
python src/model.py
The best model will be saved as best_model.pkl in the root directory.

3. Running the API
Deploy the model as a Flask API for real-time predictions:

bash
Copy
python src/app.py
The API will be hosted at http://127.0.0.1:5000.

API
1. Endpoints
GET /: Returns a welcome message.

POST /predict: Accepts customer data as JSON and returns the churn prediction.

2. Example Input for POST /predict:
json
Copy
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
Copy
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
Copy
python test_prediction.py
This script sends a POST request to the /predict endpoint with sample customer data and prints the churn prediction.

Contact
For any questions or issues, feel free to reach out:

GitHub: https://github.com/Om700-create/Telco_Churn_Predictor

Email: narayanbhandari498@gmail.com

