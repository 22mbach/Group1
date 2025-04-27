from flask import Blueprint, request, jsonify

wishlist_bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")

@wishlist_bp.route("/", methods=["GET"])
def get_wishlist():
    return jsonify({"wishlist": []})

@wishlist_bp.route("/<int:listing_id>", methods=["POST"])
def add_to_wishlist(listing_id):
    return jsonify({"message": f"Listing {listing_id} added to wishlist"})