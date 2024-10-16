# tests/test_feature_engineering.py
import unittest
import pandas as pd
from src.feature_engineering import create_features

class TestFeatureEngineering(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test case with sample data."""
        # Sample data for testing
        data = {
            'TotalCharges': [30.0, 60.0, 90.0],
            'tenure': [10, 20, 30],
            'Tenure_Category': ['0-12 Months', '1-2 Years', '2+ Years']
        }
        cls.df = pd.DataFrame(data)

    def test_create_features(self):
        """Test the feature engineering function."""
        engineered_df = create_features(self.df)

        # Check if new features were created
        self.assertIn('Charges_per_Month', engineered_df.columns)
        self.assertEqual(engineered_df['Charges_per_Month'].iloc[0], 3.0)

        # Check if dummies for 'Tenure_Category' were created
        self.assertIn('Tenure_1-2 Years', engineered_df.columns)
        self.assertIn('Tenure_2+ Years', engineered_df.columns)

if __name__ == '__main__':
    unittest.main()
