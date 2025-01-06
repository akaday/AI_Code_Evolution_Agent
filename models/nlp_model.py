from transformers import pipeline

def analyze_code_comments(code):
    nlp = pipeline("sentiment-analysis")
    result = nlp(code)
    return result
