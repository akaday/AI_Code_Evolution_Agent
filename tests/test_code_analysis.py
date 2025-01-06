import unittest
from models.nlp_model.py import analyze_code_comments

class TestCodeAnalysis(unittest.TestCase):
    def test_analyze_code_comments(self):
        result = analyze_code_comments("This function calculates the sum.")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
