import pandas as pd
from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify


from api.classes.exceptions import NoDataFoundException

launches_bp = Blueprint("launches", __name__, url_prefix="/launches")


@launches_bp.route("/get_all_launches", methods=["GET"])
def get_all_launches():
    conn = app.spacex_api
    try:
        launches = conn.get_all_launches()
    except NoDataFoundException as e:
        abort(404, description=str(e))
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launches_df = launches_df[["id", "name", "date_utc", "success", "details"]]
    launches_df["date_utc"] = pd.to_datetime(launches_df["date_utc"], utc=True)
    launches_df["year"] = launches_df["date_utc"].dt.year

    return (jsonify(launches_df.to_dict("records")), 200)


@launches_bp.route("/get_all_launchpads_with_launches", methods=["GET"])
def get_all_launchpads_with_launches():
    conn = app.spacex_api
    try:
        launches = conn.get_all_launches()
    except NoDataFoundException as e:
        abort(404, description=str(e))
    except Exception as e:
        raise e

    try:
        launchpads = conn.get_all_launchpads()
    except NoDataFoundException as e:
        abort(404, description=str(e))
    except Exception as e:
        raise e

    launches_df = pd.DataFrame(launches)
    launchpads_df = pd.DataFrame(launchpads)

    launches_df = launches_df[
        ["id", "name", "date_utc", "success", "details", "launchpad"]
    ]
    launchpads_df = launchpads_df[
        [
            "id",
            "name",
            "full_name",
            "locality",
            "status",
            "details",
            "launches",
        ]
    ]

    launchpads_df = launchpads_df.explode("launches")

    launchpads_df = launchpads_df.merge(
        launches_df,
        how="left",
        left_on="launches",
        right_on="id",
        suffixes=("_launchpad", "_launch"),
    ).drop(columns=["launches", "launchpad"])

    grouped_df = (
        launchpads_df.groupby(
            [
                "id_launchpad",
                "name_launchpad",
                "full_name",
                "locality",
                "status",
                "details_launchpad",
            ]
        )
        .apply(
            lambda x: x[
                [
                    "id_launch",
                    "name_launch",
                    "date_utc",
                    "success",
                    "details_launch",
                ]
            ].to_dict(orient="records")
        )
        .reset_index(name="launches")
    )

    return (jsonify(grouped_df.to_dict("records")), 200)
