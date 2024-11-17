from flask import Blueprint
from flask import current_app as app

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    return app.send_static_file("index.html")
