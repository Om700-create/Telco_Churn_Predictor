# src/utils.py
import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    """Plot the feature importances of the model."""
    importances = model.feature_importances_
    indices = range(len(importances))
    
    plt.figure(figsize=(12, 6))
    plt.title('Feature Importances')
    plt.bar(indices, importances, align='center')
    plt.xticks(indices, feature_names, rotation=90)
    plt.xlim([-1, len(importances)])
    plt.tight_layout()
    plt.show()

def log_model_info(model):
    """Log model information."""
    print(f"Model type: {type(model).__name__}")
    print(f"Model parameters: {model.get_params()}")
