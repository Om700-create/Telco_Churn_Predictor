# tests/test_data_processing.py
import unittest
import pandas as pd
from src.data_processing import load_data, preprocess_data

class TestDataProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test case with sample data."""
        # Create a sample DataFrame for testing
        data = {
            'customerID': ['0001', '0002', '0003'],
            'gender': ['Female', 'Male', 'Female'],
            'SeniorCitizen': [0, 1, 0],
            'tenure': [1, 2, 3],
            'MonthlyCharges': [29.85, 56.95, 53.85],
            'TotalCharges': [29.85, 56.95, 53.85]
        }
        cls.df = pd.DataFrame(data)

    def test_load_data(self):
        """Test if the data loading function works correctly."""
        df = load_data('data/telco_customer_churn.csv')  # Path to your test CSV
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(df.shape[0], 0, "DataFrame is empty")

    def test_preprocess_data(self):
        """Test the preprocessing function."""
        processed_df = preprocess_data(self.df)

        # Ensure the preprocessing function drops NaN values and encodes categorical columns
        self.assertNotIn('customerID', processed_df.columns)
        self.assertIn('gender_Male', processed_df.columns)
        self.assertEqual(processed_df.shape[0], self.df.shape[0], "Row count should remain the same after dropping NaNs")

if __name__ == '__main__':
    unittest.main()
