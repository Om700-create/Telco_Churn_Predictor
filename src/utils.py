import joblib
import logging
import os

# Set up logging in the utils module
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

def load_model(model_path):
    """
    Load the pre-trained model from the given path.
    """
    if not os.path.exists(model_path):
        logging.error(f"Model file not found at {model_path}")
        return None

    try:
        model = joblib.load(model_path)
        logging.info(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        logging.error(f"Failed to load model: {str(e)}")
        return None


def validate_input(data, required_features):
    """
    Validate the input data for missing features and correct data types.
    
    Parameters:
    - data: The input data to validate (as a dict).
    - required_features: List of required features.

    Returns:
    - error_message: If there's an error in validation, return an error message. Otherwise, return None.
    """
    # Check for missing features
    missing_features = [feature for feature in required_features if feature not in data]
    if missing_features:
        return f"Missing features: {missing_features}"
    
    # Check for invalid data types
    for feature in required_features:
        if not isinstance(data[feature], (int, float)):
            return f"Invalid data type for {feature}. Expected int or float."
    
    return None


def log_error_and_format(message, error):
    """
    Utility function to log errors and format the message for the API response.
    
    Parameters:
    - message: The message to log and format.
    - error: The exception object.

    Returns:
    - A dictionary with the formatted error message.
    """
    logging.error(f"{message}: {str(error)}")
    return {"error": f"{message}: {str(error)}"}


