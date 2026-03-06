from flask import Flask, jsonify
from src.calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/api/absolute/<number>', methods=['GET'])
def get_absolute(number):
    try:
        val = float(number)
        return jsonify({"result": calc.absolute(val)}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/api/factorial/<n>', methods=['GET'])
def get_factorial(n):
    try:
        val = int(n)
        return jsonify({"result": calc.factorial(val)}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid value or type"}), 422

if __name__ == '__main__':
    app.run(port=8080)