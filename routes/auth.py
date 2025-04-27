from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix = "/auth")

@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    #Dummy login logic
    if username == "admin" and password == "admin":
        return jsonify({"message": "Login successfully"}), 200
    return jsonify({"error": "Invalid credentials"}), 401