from flask import Blueprint, request, jsonify

listings_bp = Blueprint("listings", __name__, url_prefix = "/listings")

@listings_bp.route("/", methods = ["GET"])
def show_listings():
    return jsonify([{"id": 1, "title": "Cozy Cabin"}])

@listings_bp.route("/", methods=["POST"])
def add_listing():
    data = request.get_json()
    return jsonify({"message": "Listing added", "listing": data}), 201

@listings_bp.route("/<int:listing_id>", methods=["GET"])
def show_product(listing_id):
    return jsonify({"id": listing_id, "title": "Cozy Cabin"})