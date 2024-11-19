from flask import Blueprint
from flask import current_app as app, jsonify

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    # Serve the react app from the root URL in production
    if app.config["CONFIG_TYPE"] == "PROD":
        return app.send_static_file("index.html")

    return jsonify("Welcome to the SpaceX Python Wrapper API"), 200
