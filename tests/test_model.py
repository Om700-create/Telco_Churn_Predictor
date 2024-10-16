# tests/test_model.py
import unittest
import pandas as pd
from sklearn.datasets import make_classification
from src.model import train_model

class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test case with a synthetic dataset."""
        cls.X, cls.y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=2, random_state=42)
        cls.X = pd.DataFrame(cls.X, columns=[f'feature_{i}' for i in range(10)])
        cls.y = pd.Series(cls.y)

    def test_train_model(self):
        """Test the model training function."""
        model, report = train_model(self.X, self.y)

        # Check if the model is trained and a report is generated
        self.assertIsNotNone(model, "Model should be trained and returned")
        self.assertIn('precision', report.lower(), "Report should contain precision metrics")

if __name__ == '__main__':
    unittest.main()
