# tests/test_utils.py
import unittest
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from src.utils import plot_feature_importance

class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test case with a synthetic dataset."""
        cls.X, cls.y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=2, random_state=42)
        cls.model = RandomForestClassifier(random_state=42)
        cls.model.fit(cls.X, cls.y)

    def test_plot_feature_importance(self):
        """Test the feature importance plotting function."""
        try:
            plot_feature_importance(self.model, [f'feature_{i}' for i in range(10)])
            # If no exception is raised, the plot function is considered successful
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"plot_feature_importance raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
