import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Load Data
def load_data(filepath):
    """
    Load the final feature-engineered dataset from the specified CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        logging.error(f"File not found at {filepath}. Please check the path.")
        return None

# Data Preprocessing
def preprocess_data(df):
    """
    Preprocess the data by encoding categorical features and handling the target column.
    """
    if 'customerID' in df.columns:
        df.drop(columns=['customerID'], inplace=True)
        logging.info("'customerID' column removed.")

    # Ensure all columns are numeric (convert categorical columns if necessary)
    categorical_columns = df.select_dtypes(include=['object']).columns
    if len(categorical_columns) > 0:
        logging.info(f"Non-numeric columns still present: {categorical_columns.tolist()}. Encoding them.")
        df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
        logging.info("Categorical columns encoded.")

    return df

# Split Data
def split_data(df, target_column='Churn_Yes'):
    """
    Split the data into features and target, then into training and testing sets.
    """
    if target_column not in df.columns:
        logging.error(f"Target column '{target_column}' not found in the dataset.")
        return None, None, None, None

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logging.info("Data split into training and testing sets.")
    return X_train, X_test, y_train, y_test

# Hyperparameter Tuning for Logistic Regression
def tune_logistic_regression(X_train, y_train):
    """
    Perform hyperparameter tuning on Logistic Regression using GridSearchCV.
    """
    model = LogisticRegression(max_iter=1000)
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'solver': ['liblinear', 'lbfgs']
    }
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    logging.info(f"Best Logistic Regression Params: {grid_search.best_params_}")
    logging.info("Logistic Regression model tuned.")
    return grid_search.best_estimator_

# Hyperparameter Tuning for Random Forest
def tune_random_forest(X_train, y_train):
    """
    Perform hyperparameter tuning on Random Forest using GridSearchCV.
    """
    model = RandomForestClassifier(random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10]
    }
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    logging.info(f"Best Random Forest Params: {grid_search.best_params_}")
    logging.info("Random Forest model tuned.")
    return grid_search.best_estimator_

# Hyperparameter Tuning for SVM
def tune_svm(X_train, y_train):
    """
    Perform hyperparameter tuning on SVM using GridSearchCV.
    """
    model = SVC()
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'rbf']
    }
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    logging.info(f"Best SVM Params: {grid_search.best_params_}")
    logging.info("SVM model tuned.")
    return grid_search.best_estimator_

# Evaluation Function
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model performance and return the metrics.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"Model Accuracy: {accuracy:.4f}")
    logging.info(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    logging.info(f"Classification Report:\n{classification_report(y_test, y_pred)}")
    return accuracy

# Save Best Model
def save_best_model(model, filename='best_model.pkl'):
    """
    Save the best model to a pickle file for future use.
    """
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    logging.info(f"Best model saved to {filename}")

# Main Function
def main():
    # Filepath for the feature-engineered dataset
    final_data_path = "C:/project/Telco_Churn_Predictor/data/processed/telco_customer_churn_final.csv"
    
    # Load and preprocess the data
    df = load_data(final_data_path)
    if df is None:
        return

    df = preprocess_data(df)
    
    # Split the data
    X_train, X_test, y_train, y_test = split_data(df, target_column='Churn_Yes')

    # Hyperparameter Tuning and Model Evaluation
    logging.info("Tuning Logistic Regression model...")
    tuned_logistic_model = tune_logistic_regression(X_train, y_train)
    logging.info("Evaluating tuned Logistic Regression model...")
    logistic_accuracy = evaluate_model(tuned_logistic_model, X_test, y_test)

    logging.info("Tuning Random Forest model...")
    tuned_rf_model = tune_random_forest(X_train, y_train)
    logging.info("Evaluating tuned Random Forest model...")
    rf_accuracy = evaluate_model(tuned_rf_model, X_test, y_test)

    logging.info("Tuning SVM model...")
    tuned_svm_model = tune_svm(X_train, y_train)
    logging.info("Evaluating tuned SVM model...")
    svm_accuracy = evaluate_model(tuned_svm_model, X_test, y_test)

    # Choose the best model based on accuracy
    accuracies = {
        "Logistic Regression": logistic_accuracy,
        "Random Forest": rf_accuracy,
        "SVM": svm_accuracy
    }
    
    best_model_name = max(accuracies, key=accuracies.get)
    best_model = {
        "Logistic Regression": tuned_logistic_model,
        "Random Forest": tuned_rf_model,
        "SVM": tuned_svm_model
    }[best_model_name]

    logging.info(f"Best Model: {best_model_name} with accuracy: {accuracies[best_model_name]:.4f}")
    
    # Save the best model
    save_best_model(best_model)

if __name__ == "__main__":
    main()



