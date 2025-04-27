from flask import Blueprint, jsonify

recommend_bp = Blueprint("recommend", __name__, url_prefix="/recommendations")

@recommend_bp.route("/", methods=["GET"])
def get_recommendations():
    return jsonify({"recommendations": ["Modern Loft", "Seaside Villa"]})