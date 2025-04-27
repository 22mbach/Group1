from flask import Blueprint, jsonify

static_bp = Blueprint("static", __name__)

@static_bp.route("/contact", methods=["GET"])
def show_contact():
    return jsonify({"email": "support@staybnb.com", "phone": "123-456-7890"})

@static_bp.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Staybnb Root Page - Go to /homepage"})
