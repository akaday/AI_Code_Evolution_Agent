import subprocess
import json
from models.nlp_model import analyze_code_comments

def run_tool(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

def parse_pylint_output(output):
    # Parse pylint output
    pylint_issues = []
    for line in output.splitlines():
        if line.startswith("************* Module"):
            continue
        parts = line.split(":")
        if len(parts) >= 4:
            pylint_issues.append({
                "file": parts[0],
                "line": int(parts[1]),
                "type": parts[2].strip(),
                "message": ":".join(parts[3:]).strip()
            })
    return pylint_issues

def parse_flake8_output(output):
    # Parse flake8 output
    flake8_issues = []
    for line in output.splitlines():
        parts = line.split(":")
        if len(parts) >= 4:
            flake8_issues.append({
                "file": parts[0],
                "line": int(parts[1]),
                "type": parts[2].strip(),
                "message": ":".join(parts[3:]).strip()
            })
    return flake8_issues

def parse_mypy_output(output):
    # Parse mypy output
    mypy_issues = []
    for line in output.splitlines():
        parts = line.split(":")
        if len(parts) >= 4:
            mypy_issues.append({
                "file": parts[0],
                "line": int(parts[1]),
                "type": parts[2].strip(),
                "message": ":".join(parts[3:]).strip()
            })
    return mypy_issues

def parse_bandit_output(output):
    # Parse bandit output
    bandit_issues = []
    for line in output.splitlines():
        if line.startswith("["):
            parts = line.split("]")
            if len(parts) >= 2:
                bandit_issues.append({
                    "type": parts[0].strip("[]"),
                    "message": parts[1].strip()
                })
    return bandit_issues

def detect_code_smells():
    pylint_output = run_tool(["pylint", "src"])
    flake8_output = run_tool(["flake8", "src"])
    mypy_output = run_tool(["mypy", "src"])
    bandit_output = run_tool(["bandit", "-r", "src"])

    pylint_issues = parse_pylint_output(pylint_output)
    flake8_issues = parse_flake8_output(flake8_output)
    mypy_issues = parse_mypy_output(mypy_output)
    bandit_issues = parse_bandit_output(bandit_output)

    # Custom code smell detection using NLP model
    custom_issues = []
    with open("data/datasets/example_dataset.json", "r") as f:
        dataset = json.load(f)
        for item in dataset:
            comment_analysis = analyze_code_comments(item["comment"])
            if comment_analysis != "positive":
                custom_issues.append({
                    "file": "unknown",
                    "line": "unknown",
                    "type": "custom",
                    "message": f"Potential issue in comment: {item['comment']}"
                })

    return {
        "pylint": pylint_issues,
        "flake8": flake8_issues,
        "mypy": mypy_issues,
        "bandit": bandit_issues,
        "custom": custom_issues
    }
