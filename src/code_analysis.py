import pylint.lint
import flake8.main.application
import subprocess
import json

def analyze_code(code):
    analysis = {
        "length": len(code),
        "lines": code.count('\n'),
        "functions": code.count('def ')
    }

    pylint_output = run_pylint_analysis(code)
    flake8_output = run_flake8_analysis(code)
    sonarqube_output = run_sonarqube_analysis(code)

    analysis["pylint"] = pylint_output
    analysis["flake8"] = flake8_output
    analysis["sonarqube"] = sonarqube_output

    return analysis

def run_pylint_analysis(code):
    pylint_opts = ['--output-format=json']
    pylint_output = pylint.lint.Run(pylint_opts, do_exit=False)
    return parse_pylint_output(pylint_output.linter.reporter.data)

def parse_pylint_output(output):
    parsed_output = []
    for item in output:
        parsed_output.append({
            "type": item['type'],
            "module": item['module'],
            "obj": item['obj'],
            "line": item['line'],
            "message": item['message']
        })
    return parsed_output

def run_flake8_analysis(code):
    app = flake8.main.application.Application()
    app.initialize(['--format=json'])
    app.run_checks([code])
    app.report()
    return parse_flake8_output(app.formatter.output_fd.getvalue())

def parse_flake8_output(output):
    parsed_output = json.loads(output)
    return parsed_output

def run_sonarqube_analysis(code):
    result = subprocess.run(['sonar-scanner'], capture_output=True, text=True)
    return parse_sonarqube_output(result.stdout)

def parse_sonarqube_output(output):
    parsed_output = []
    for line in output.split('\n'):
        if line.startswith('INFO:'):
            parsed_output.append(line)
    return parsed_output
