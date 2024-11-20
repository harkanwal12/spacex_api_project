import numpy as np
import pandas as pd
from flask import Blueprint
from flask import current_app as app
from flask import json, jsonify
from werkzeug.exceptions import HTTPException, NotFound

from api.classes.exceptions import NoDataFoundException
from api.classes.spacex import SpaceX

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/")
def api_home():
    return jsonify("Welcome to the SpaceX Python Wrapper API"), 200


@api_bp.route("/get_all_launch_years", methods=["GET"])
def get_all_launch_years():
    conn = app.spacex_api

    query = {
        "query": {},
        "options": {
            "pagination": False,
            "select": {"date_utc": 1, "id": 1},
        },
    }

    try:
        launches = conn.get_launches(query=query)
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df["date_utc"] = pd.to_datetime(launches_df["date_utc"], utc=True)
    unique_years = launches_df["date_utc"].dt.year.unique()

    return jsonify(unique_years.tolist()), 200


@api_bp.route("/<year>/get_all_launches_in_year", methods=["GET"])
def get_all_launches_in_year(year):
    conn = app.spacex_api

    year = pd.Timestamp(year)
    next_year = year.replace(year=year.year + 1)

    query = {
        "query": {"date_utc": {"$gte": str(year), "$lt": str(next_year)}},
        "options": {
            "pagination": False,
        },
    }

    try:
        launches = conn.get_launches(query=query)
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df["date_utc"] = pd.to_datetime(launches_df["date_utc"], utc=True)
    links_df = pd.json_normalize(launches_df["links"])
    launches_df = pd.concat(
        [
            launches_df.drop(columns=["links"]),
            links_df[
                ["webcast", "wikipedia", "patch.small", "reddit.recovery"]
            ],
        ],
        axis=1,
    )
    launches_df = launches_df[
        [
            "id",
            "success",
            "details",
            "name",
            "date_utc",
            "webcast",
            "wikipedia",
            "patch.small",
            "reddit.recovery",
        ]
    ].rename(columns={"patch.small": "patch", "reddit.recovery": "reddit"})

    return jsonify(launches_df.to_dict("records")), 200


@api_bp.route("/get_all_launchpad_names", methods=["GET"])
def get_all_launchpad_names():
    conn = app.spacex_api
    query = {
        "query": {},
        "options": {
            "pagination": False,
            "select": {"id": 1, "name": 1, "full_name": 1},
        },
    }
    try:
        launches = conn.get_launchpads(query=query)
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df = launches_df[["name", "full_name", "id"]]
    return jsonify(launches_df.to_dict("records")), 200


@api_bp.route("/<id>/<shortname>/get_launchpad_with_launches")
def get_launchpad_with_launches(id, shortname):
    conn = app.spacex_api

    query = {
        "query": {
            "id": {"$eq": id},
            "name": {"$eq": shortname},
        },
        "options": {
            "populate": ["launches"],
            "pagination": False,
            "select": {
                "rockets": 0,
                "timezone": 0,
            },
        },
    }

    try:
        launchpad = conn.get_launchpads(query=query)
    except Exception as e:
        raise e

    launchpad = pd.DataFrame(launchpad)

    launchpad = launchpad[
        [
            "id",
            "name",
            "full_name",
            "locality",
            "status",
            "launches",
            "images",
            "details",
            "launch_attempts",
            "launch_successes",
            "region",
            "latitude",
            "longitude",
        ]
    ]

    launchpad["images"] = launchpad["images"].apply(lambda x: x["large"][0])
    launchpad["launch_success_rate"] = success_rate_calculator(
        successes=launchpad["launch_successes"][0],
        attempts=launchpad["launch_attempts"][0],
    )

    return jsonify(launchpad.to_dict("records")), 200


@api_bp.errorhandler(Exception)
def handle_exception(error):
    if isinstance(error, HTTPException):
        # Create a response
        response = error.get_response()
        response.data = json.dumps(
            {
                "code": error.code,
                "name": error.name,
                "description": error.description,
            }
        )
        response.content_type = "application/json"
        return response

    if isinstance(error, NoDataFoundException):
        return (
            jsonify("No data was found"),
            404,
        )

    return (
        jsonify(
            "Unknown error occurred, please contact API developers for assistance"
        ),
        500,
    )


@staticmethod
def success_rate_calculator(attempts: int, successes: int) -> str:
    if not (attempts or successes):
        return "N/A"

    try:
        rate = successes / attempts * 100
    except Exception:
        return "N/A"

    if not np.isnan(rate):
        return str(int(rate)) + "%"
    else:
        return "N/A"
