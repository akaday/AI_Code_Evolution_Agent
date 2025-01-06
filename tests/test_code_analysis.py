import unittest
from models.nlp_model import analyze_code_comments
from src.code_analysis import analyze_code

class TestCodeAnalysis(unittest.TestCase):
    def test_analyze_code_comments(self):
        result = analyze_code_comments("This function calculates the sum.")
        self.assertIsNotNone(result)

    def test_analyze_code(self):
        code = """
        def add(a, b):
            return a + b
        """
        result = analyze_code(code)
        self.assertIn("length", result)
        self.assertIn("lines", result)
        self.assertIn("functions", result)
        self.assertIn("pylint", result)
        self.assertIn("flake8", result)
        self.assertIn("sonarqube", result)

if __name__ == "__main__":
    unittest.main()
