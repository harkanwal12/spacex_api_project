import pandas as pd
from flask import Blueprint
from flask import current_app as app
from flask import jsonify
from werkzeug.exceptions import NotFound
import numpy as np


from api.classes.exceptions import NoDataFoundException
from api.classes.spacex import SpaceX

launches_bp = Blueprint("launches", __name__, url_prefix="/api")

# TODO swap out SpaceX module with one from app instance


@launches_bp.route("/get_all_launch_years", methods=["GET"])
def get_all_launch_years():
    conn = SpaceX(ssl_verify=False)

    query = {
        "query": {},
        "options": {
            "pagination": False,
            "select": {"date_utc": 1, "id": 1},
        },
    }

    try:
        launches = conn.get_launches(query=query)
    except NoDataFoundException as e:
        raise NotFound("No data found for request")
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df["date_utc"] = pd.to_datetime(launches_df["date_utc"], utc=True)
    unique_years = launches_df["date_utc"].dt.year.unique()

    return jsonify(unique_years.tolist()), 200


@launches_bp.route("/<year>/get_all_launches_in_year", methods=["GET"])
def get_all_launches_in_year(year):
    conn = SpaceX(ssl_verify=False)

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
    except NoDataFoundException as e:
        raise NotFound("No data found for request")
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df["date_utc"] = pd.to_datetime(launches_df["date_utc"], utc=True)
    launches_df["patch"] = launches_df["links"].apply(
        lambda x: x["patch"]["small"]
    )
    launches_df = launches_df[
        ["id", "success", "details", "name", "date_utc", "patch"]
    ]

    return jsonify(launches_df.to_dict("records")), 200


@launches_bp.route("/get_all_launchpad_names", methods=["GET"])
def get_all_launchpad_names():
    conn = SpaceX(ssl_verify=False)
    query = {
        "query": {},
        "options": {
            "pagination": False,
            "select": {"id": 1, "name": 1, "full_name": 1},
        },
    }
    try:
        launches = conn.get_launchpads(query=query)
    except NoDataFoundException as e:
        raise NotFound("No data found for request")
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df = launches_df[["name", "full_name", "id"]]
    return jsonify(launches_df.to_dict("records")), 200


@launches_bp.route("/<id>/<shortname>/get_launchpad_with_launches")
def get_launchpad_with_launches(id, shortname):
    conn = SpaceX(ssl_verify=False)

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
    except NoDataFoundException as e:
        raise NotFound("No data found for request")
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
    launchpad["launch_success_rate"] = (
        launchpad["launch_successes"] / launchpad["launch_attempts"]
    ) * 100
    if not np.isnan(launchpad["launch_success_rate"][0]):
        launchpad["launch_success_rate"] = launchpad[
            "launch_success_rate"
        ].round()
        launchpad["launch_success_rate"] = (
            launchpad["launch_success_rate"].astype(int).astype(str) + "%"
        )
    else:
        launchpad["launch_success_rate"] = "N/A"

    return jsonify(launchpad.to_dict("records")), 200
