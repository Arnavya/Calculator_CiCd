from flask import Blueprint, request, jsonify, render_template
from .calculator import add, subtract, multiply, divide

calc_bp = Blueprint("calculator", __name__, template_folder="templates")


@calc_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@calc_bp.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    a = float(data["a"])
    b = float(data["b"])
    operation = data["operation"]

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})
