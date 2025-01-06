# Setup Guide

## Installation
1. Clone the repository: `git clone https://github.com/your-username/AI_Code_Evolution_Agent.git`
2. Navigate to the project directory: `cd AI_Code_Evolution_Agent`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the main script: `python src/main.py`

## Code Analysis Setup
To run code analysis with pylint, flake8, and SonarQube, follow these steps:

### Pylint
1. Install pylint: `pip install pylint`
2. Create a `.pylintrc` configuration file in the root directory of the repository to customize pylint's behavior.
3. Run pylint: `pylint <your_python_file.py>`

### Flake8
1. Install flake8: `pip install flake8`
2. Create a `.flake8` configuration file in the root directory of the repository to customize flake8's behavior.
3. Run flake8: `flake8 <your_python_file.py>`

### SonarQube
1. Install SonarQube and SonarScanner by following the official SonarQube documentation.
2. Configure SonarQube by setting up a `sonar-project.properties` file in the root directory of the repository. This file should include the necessary project settings and paths.
3. Run SonarQube analysis: `sonar-scanner`
