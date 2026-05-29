"""
DEMO FILE: Contains 10 intentional errors for CI/CD validation
Each error will be caught by ruff or bandit
"""

# ❌ ERROR 1: Unsorted imports (ruff I001)
from flask import Flask, jsonify
import os
import sys
from models import db

# ❌ ERROR 2: Unused import (ruff F401)
import json

# ❌ ERROR 3: Unused import (ruff F401)
import pickle

# ❌ ERROR 4: Another unused import (ruff F401)
import subprocess

app = Flask(__name__)

# ❌ ERROR 5: Flask debug=True (bandit B201 - HIGH severity)
app.run(debug=True)

# ❌ ERROR 6: Hardcoded password (bandit - security issue)
PASSWORD = "admin123password"

# ❌ ERROR 7: Line too long (ruff E501 - exceeds 100 chars)
very_long_variable_name_that_exceeds_the_line_length_limit_of_100_characters_which_is_configured = "intentionally too long"

# ❌ ERROR 8: eval() usage (bandit B307 - MEDIUM severity)
def evaluate_code(user_input):
    result = eval(user_input)
    return result

# ❌ ERROR 9: pickle.loads() (bandit B301 - MEDIUM severity)
def deserialize_data(data):
    return pickle.loads(data)

# ❌ ERROR 10: subprocess with shell=True (bandit B602 - HIGH severity)
def run_command(cmd):
    import subprocess
    return subprocess.run(cmd, shell=True)

@app.route('/')
def home():
    return "Hello"

# ❌ BONUS ERROR 11: Unused variable (ruff F841)
@app.route('/test')
def test():
    unused_data = "not used"
    return "test"

if __name__ == '__main__':
    app.run()
