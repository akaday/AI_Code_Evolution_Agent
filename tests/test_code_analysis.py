import unittest
from models.nlp_model import analyze_code_comments
from src.code_analysis import detect_code_smells

class TestCodeAnalysis(unittest.TestCase):
    def test_analyze_code_comments(self):
        result = analyze_code_comments("This function calculates the sum.")
        self.assertIsNotNone(result)

    def test_detect_code_smells(self):
        result = detect_code_smells()
        self.assertIn("pylint", result)
        self.assertIn("flake8", result)
        self.assertIn("mypy", result)
        self.assertIn("bandit", result)
        self.assertIn("custom", result)
        self.assertIsInstance(result["pylint"], list)
        self.assertIsInstance(result["flake8"], list)
        self.assertIsInstance(result["mypy"], list)
        self.assertIsInstance(result["bandit"], list)
        self.assertIsInstance(result["custom"], list)

if __name__ == "__main__":
    unittest.main()
