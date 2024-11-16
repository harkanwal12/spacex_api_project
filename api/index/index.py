from flask import Blueprint, jsonify, json
from api.classes.connection import SpacexConnection
from werkzeug.exceptions import HTTPException

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    return jsonify(
        {"message": "Welcome to the SpaceX Python Wrapper API"}, 200
    )


@index_bp.route("/get_company_info", methods=["GET"])
def get_company_info():
    conn = SpacexConnection()
    # add exception handling for return

    company_info = conn.get_company_info()

    return (
        jsonify(company_info.to_dict()),
        200,
    )


@index_bp.errorhandler(404)
def no_data_found(error):
    return jsonify(error.description), 404


@index_bp.errorhandler(Exception)
def handle_exception(error):
    if isinstance(error, HTTPException):
        return error

    return jsonify(error=str(error)), 500
