from flask import Blueprint
from api.classes.connection import SpacexConnection

launches_bp = Blueprint("launches", __name__, url_prefix="/launches")


@launches_bp.route("/hello", methods=["GET"])
def hello():
    conn = SpacexConnection()
    # add exception handling for return
    response = conn.get_company_info()
    return response
