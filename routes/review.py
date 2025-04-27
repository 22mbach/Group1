from flask import Blueprint, request, jsonify

review_bp = Blueprint("review", __name__, url_prefix="/reviews")

@review_bp.route("/<int:listing_id>", methods=["GET"])
def show_reviews(listing_id):
    return jsonify({"listing_id": listing_id, "reviews": []})

@review_bp.route("/<int:listing_id>", methods=["POST"])
def add_review(listing_id):
    data = request.get_json()
    return jsonify({"message": "Review added", "review": data})