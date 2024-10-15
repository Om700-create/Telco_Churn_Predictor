import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "data/telco_customer_churn.csv",  # Raw dataset
    "data/processed/__init__.py",  # Processed data placeholder
    "notebooks/01_data_exploration.ipynb",  # Exploratory Data Analysis
    "notebooks/02_feature_engineering.ipynb",  # Feature engineering process
    "notebooks/03_model_training.ipynb",  # Model training and evaluation
    "notebooks/04_model_deployment.ipynb",  # Deployment considerations
    "notebooks/05_results_analysis.ipynb",  # Results interpretation and visualization
    "src/__init__.py",  # Package initialization
    "src/data_processing.py",  # Data cleaning and preprocessing functions
    "src/feature_engineering.py",  # Feature engineering functions
    "src/model.py",  # Model definition and training
    "src/utils.py",  # Utility functions (e.g., for visualization)
    "src/app.py",  # Main application file
    "tests/test_data_processing.py",  # Tests for data processing functions
    "tests/test_feature_engineering.py",  # Tests for feature engineering functions
    "tests/test_model.py",  # Tests for model training and evaluation
    "tests/test_utils.py",  # Tests for utility functions
    "requirements.txt",  # List of dependencies for the project
    "setup.py",  # Setup script for packaging the project
    "README.md",  # Project overview and documentation
    "LICENSE",  # License file for the project (e.g., MIT License)
    ".gitignore",  # Files/folders to ignore in Git
]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")
