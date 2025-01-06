import unittest
from src.code_analysis import analyze_code

class TestCodeAnalysis(unittest.TestCase):
    def test_analyze_code(self):
        code = '''
        def add(a, b):
            return a + b
        '''
        analysis = analyze_code(code)
        self.assertIn("length", analysis)
        self.assertIn("lines", analysis)
        self.assertIn("functions", analysis)
        self.assertIn("code_smells", analysis)
        self.assertIn("pylint", analysis)
        self.assertIn("flake8", analysis)
        self.assertIn("sonarqube", analysis)

if __name__ == "__main__":
    unittest.main()
