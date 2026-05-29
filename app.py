"""TEMPORARILY MODIFIED - Added intentional issues for CI/CD validation."""

from flask import Flask, jsonify, render_template, request
import os
import pickle
import subprocess
import json
import sys
from models import Product, db

# ❌ SECURITY ISSUE 1: Hardcoded password
DB_PASSWORD = "admin123456789"

# ❌ SECURITY ISSUE 2: Debug mode enabled
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.run(debug=True)  # HIGH severity - should not be True in production

db.init_app(app)

# ❌ SECURITY ISSUE 3: Using eval() - B307
@app.route('/evaluate', methods=['POST'])
def evaluate():
    """Dangerous eval usage."""
    data = request.json
    user_input = data.get('code')
    result = eval(user_input)  # DANGEROUS - will be caught by bandit B307
    return {"result": result}

# ❌ SECURITY ISSUE 4: Using pickle.loads - B301
@app.route('/deserialize', methods=['POST'])
def deserialize():
    """Unsafe pickle deserialization."""
    data = request.json
    obj = pickle.loads(data.get('data'))  # DANGEROUS - will be caught by bandit B301
    return {"result": obj}

# ❌ SECURITY ISSUE 5: Subprocess with shell=True - B602
@app.route('/execute', methods=['POST'])
def execute_command():
    """Unsafe subprocess execution."""
    command = request.json.get('cmd')
    result = subprocess.run(command, shell=True)  # DANGEROUS - bandit B602
    return {"output": str(result)}

# ❌ LINTING ISSUE: Long line exceeding 100 characters
very_long_variable_name_that_exceeds_the_line_length_limit_of_100_characters_because_it_is_intentionally_too_long = "This line is intentionally too long to test ruff detection"

# ❌ LINTING ISSUE: Unused imports
print(json)  # Using json to avoid "unused import" but it's not used properly

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    return {"message": "Product added"}

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return {"products": [p.to_dict() for p in products], "count": len(products)}

if __name__ == '__main__':
    app.run(debug=True)
