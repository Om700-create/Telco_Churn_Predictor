import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the processed dataset
df = pd.read_csv("C:/project/Telco_Churn_Predictor/notebooks/telco_customer_churn_processed.csv")

# Convert 'Tenure_Category' to numerical using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Tenure_Category'], drop_first=True)

# Define features and target variable
X = df_encoded.drop(columns=['Churn_Yes'])  # Exclude target column
y = df_encoded['Churn_Yes']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(),
    "Support Vector Machine": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

 #Initialize a dictionary to hold results
results = {}

for model_name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    # Store the results
    results[model_name] = {
        'Confusion Matrix': cm,
        'Classification Report': report,
        'Accuracy': report['accuracy']
    }

    # Print the results
    print(f"Model: {model_name}")
    print("Confusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print(f"Accuracy: {report['accuracy']:.4f}\n")


# Define parameter grid for Logistic Regression
lr_param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['liblinear', 'saga']
}

# Initialize Grid Search for Logistic Regression
lr_grid = GridSearchCV(LogisticRegression(max_iter=1000), lr_param_grid, cv=5, scoring='accuracy', n_jobs=-1)
lr_grid.fit(X_train, y_train)

# Best parameters and score
print("Best parameters for Logistic Regression:", lr_grid.best_params_)
print("Best accuracy for Logistic Regression:", lr_grid.best_score_)


# Define parameter grid for Random Forest
rf_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Initialize Grid Search for Random Forest
rf_grid = GridSearchCV(RandomForestClassifier(), rf_param_grid, cv=5, scoring='accuracy', n_jobs=-1)
rf_grid.fit(X_train, y_train)

# Best parameters and score
print("Best parameters for Random Forest:", rf_grid.best_params_)
print("Best accuracy for Random Forest:", rf_grid.best_score_)

# Define parameter grid for Support Vector Machine
svm_param_grid = {
    'C': [0.01, 0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}

# Initialize Grid Search for SVM
svm_grid = GridSearchCV(SVC(), svm_param_grid, cv=5, scoring='accuracy', n_jobs=-1)
svm_grid.fit(X_train, y_train)

# Best parameters and score
print("Best parameters for Support Vector Machine:", svm_grid.best_params_)
print("Best accuracy for Support Vector Machine:", svm_grid.best_score_)

# Define parameter grid for K-Nearest Neighbors
knn_param_grid = {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance']
}

# Initialize Grid Search for KNN
knn_grid = GridSearchCV(KNeighborsClassifier(), knn_param_grid, cv=5, scoring='accuracy', n_jobs=-1)
knn_grid.fit(X_train, y_train)

# Best parameters and score
print("Best parameters for K-Nearest Neighbors:", knn_grid.best_params_)
print("Best accuracy for K-Nearest Neighbors:", knn_grid.best_score_)

# Define parameter grid for Decision Tree
dt_param_grid = {
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Initialize Grid Search for Decision Tree
dt_grid = GridSearchCV(DecisionTreeClassifier(), dt_param_grid, cv=5, scoring='accuracy', n_jobs=-1)
dt_grid.fit(X_train, y_train)

# Best parameters and score
print("Best parameters for Decision Tree:", dt_grid.best_params_)
print("Best accuracy for Decision Tree:", dt_grid.best_score_)


# Collect best models and their accuracies
best_models = {
    "Logistic Regression": lr_grid.best_estimator_,
    "Random Forest": rf_grid.best_estimator_,
    "Support Vector Machine": svm_grid.best_estimator_,
    "Decision Tree": dt_grid.best_estimator_,
    "K-Nearest Neighbors": knn_grid.best_estimator_
}

# Initialize a dictionary to hold final results
final_results = {}

for model_name, model in best_models.items():
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    report = classification_report(y_test, y_pred, output_dict=True)
    
    # Store the results
    final_results[model_name] = {
        'Accuracy': report['accuracy'],
        'Confusion Matrix': confusion_matrix(y_test, y_pred),
        'Classification Report': report
    }

# Display model accuracy comparison
accuracy_df = pd.DataFrame({
    'Model': final_results.keys(),
    'Accuracy': [result['Accuracy'] for result in final_results.values()]
})

print(accuracy_df)

# Save the best performing model (for example, Random Forest)
best_model = rf_grid.best_estimator_
joblib.dump(best_model, 'best_random__model.pkl')
print("Best model saved successfully.")
