from flask import Blueprint, request, jsonify

payment_bp = Blueprint("payment", __name__, url_prefix="/payment")

@payment_bp.route("/process", methods=["POST"])
def process_payment():
    return jsonify({"message": "Payment processed successfully"})