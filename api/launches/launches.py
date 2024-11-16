from flask import Blueprint, jsonify
from api.classes.connection import SpacexConnection
import pandas as pd

launches_bp = Blueprint("launches", __name__, url_prefix="/launches")


@launches_bp.route("/get_all_launches_with_sites", methods=["GET"])
def get_all_launches_with_sites():
    conn = SpacexConnection()
    launches = conn.get_all_launches()
    launchpads = conn.get_all_launchpads()

    launches_and_launchpads = pd.merge(
        launches,
        launchpads,
        how="inner",
        left_on="launchpad",
        right_on="id",
        suffixes=("_launch", "_launchpad"),
    ).drop(columns=["launchpad"])

    return (jsonify(launches_and_launchpads.to_dict("records")), 200)
