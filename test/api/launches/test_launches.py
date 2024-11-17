from api.classes.exceptions import NoDataFoundException
from werkzeug.exceptions import Unauthorized


def test_get_all_launches_success(mock_app, example_launches):
    mock_app.spacex_api.get_all_launches.return_value = example_launches
    response = mock_app.test_client().get("/launches/get_all_launches")

    expected_response = [
        {
            "date_utc": "Fri, 24 Mar 2006 22:30:00 GMT",
            "id": "5eb87cd9ffd86e000604b32a",
            "name": "FalconSat",
            "success": False,
        },
        {
            "date_utc": "Wed, 21 Mar 2007 01:10:00 GMT",
            "id": "5eb87cdaffd86e000604b32b",
            "name": "DemoSat",
            "success": False,
        },
    ]

    assert response.status_code == 200
    assert response.json == expected_response


def test_get_all_launches_error_404(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = NoDataFoundException

    response = mock_app.test_client().get("/launches/get_all_launches")

    assert response.status_code == 404
    assert response.json == "Request returned no results"


def test_get_all_launches_unknown_exception(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = Exception

    response = mock_app.test_client().get("/launches/get_all_launches")

    assert response.status_code == 500
    assert (
        response.json
        == "Unknown error occurred, please contact API developers for assistance"
    )


def test_get_all_launches_with_http_exception(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = Unauthorized

    response = mock_app.test_client().get("/launches/get_all_launches")

    assert response.status_code == 401
    assert response.json["name"] == "Unauthorized"


def test_get_all_launchpads_with_launches(
    mock_app, example_launches, example_launchpads
):
    mock_app.spacex_api.get_all_launches.return_value = example_launches
    mock_app.spacex_api.get_all_launchpads.return_value = example_launchpads
    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    expected_response = [
        {
            "details": "test launchsite with launch",
            "full_name": "Vandenberg Space Force Base Space Launch Complex 3W",
            "id_launchpad": "5e9e4501f5090910d4566f83",
            "images": "https://i.imgur.com/7uXe1Kv.png",
            "launch_attempts": 0,
            "launches": [
                {
                    "date_utc": "Fri, 24 Mar 2006 22:30:00 GMT",
                    "id_launch": "5eb87cd9ffd86e000604b32a",
                    "name_launch": "FalconSat",
                    "success": False,
                }
            ],
            "locality": "Vandenberg Space Force Base",
            "name_launchpad": "VAFB SLC 3W",
            "status": "retired",
        },
        {
            "details": "somedetails",
            "full_name": "test name",
            "id_launchpad": "test_id_2",
            "images": "https://i.imgur.com/7uXe1Kv.png",
            "launch_attempts": 0,
            "launches": [],
            "locality": "test Force Base",
            "name_launchpad": "other",
            "status": "retired",
        },
    ]

    assert response.status_code == 200
    assert response.json == expected_response


def test_get_all_launchpads_with_launches_error_404(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = [
        NoDataFoundException,
        "something",
    ]
    mock_app.spacex_api.get_all_launchpads.side_effect = NoDataFoundException

    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    assert response.status_code == 404
    assert response.json == "Request returned no results"

    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    assert response.status_code == 404
    assert response.json == "Request returned no results"


def test_get_all_launchpads_with_launches_unknown_exception(
    mock_app,
):
    mock_app.spacex_api.get_all_launches.side_effect = [Exception, "something"]
    mock_app.spacex_api.get_all_launchpads.side_effect = Exception

    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    assert response.status_code == 500
    assert (
        response.json
        == "Unknown error occurred, please contact API developers for assistance"
    )

    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    assert response.status_code == 500
    assert (
        response.json
        == "Unknown error occurred, please contact API developers for assistance"
    )


def test_get_all_launchpads_with_launches_http_exception(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = [
        Unauthorized,
        "something",
    ]
    mock_app.spacex_api.get_all_launchpads.side_effect = Unauthorized

    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    assert response.status_code == 401
    assert response.json["name"] == "Unauthorized"

    response = mock_app.test_client().get(
        "/launches/get_all_launchpads_with_launches"
    )

    assert response.status_code == 401
    assert response.json["name"] == "Unauthorized"
