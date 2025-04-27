from flask import Blueprint, request, jsonify

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

@cart_bp.route("/", methods=["GET"])
def show_cart():
    return jsonify({"cart": []})

@cart_bp.route("/", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    return jsonify({"message": "Item added to cart", "item": data})

@cart_bp.route("/<int:item_id>", methods=["DELETE"])
def remove_from_cart(item_id):
    return jsonify({"message": f"Item {item_id} removed"})