from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_bp
from routes.listings import listings_bp
from routes.cart import cart_bp
from routes.payment import payment_bp
from routes.review import review_bp
from routes.wishlist import wishlist_bp
from routes.recommend import recommend_bp
from routes.static_pages import static_bp


app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(listings_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(review_bp)
app.register_blueprint(wishlist_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(static_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")