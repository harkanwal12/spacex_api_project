from flask import Blueprint, jsonify

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    return jsonify("Welcome to the SpaceX Python Wrapper API"), 200
