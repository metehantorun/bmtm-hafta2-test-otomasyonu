from flask import Flask, jsonify, request
from src.calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/api/absolute/<number>', methods=['GET'])
def get_absolute(number):
    result = calc.absolute(float(number))
    return jsonify({"result": result}), 200

@app.route('/api/factorial/<n>', methods=['GET'])
def get_factorial(n):
    try:
        val = int(n)
        result = calc.factorial(val)
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"error": "Negative value"}), 422
    except TypeError:
        return jsonify({"error": "Invalid type"}), 422