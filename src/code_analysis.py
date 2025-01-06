def analyze_code(code):
    # Dummy analysis
    analysis = {
        "length": len(code),
        "lines": code.count('\n'),
        "functions": code.count('def ')
    }
    return analysis
