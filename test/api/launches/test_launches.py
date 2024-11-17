from api.classes.exceptions import NoDataFoundException
from werkzeug.exceptions import Unauthorized


def test_launches_get_all_launches_success(mock_app, example_launches):
    mock_app.spacex_api.get_all_launches.return_value = example_launches
    response = mock_app.test_client().get("/launches/get_all_launches")

    required_keys = ["id", "name", "date_utc", "success"]

    assert response.status_code == 200
    assert all(
        all(key in launch for key in required_keys) for launch in response.json
    )
    assert response.json[0]["date_utc"] == "Fri, 24 Mar 2006 22:30:00 GMT"
    assert not response.json[0]["success"]


def test_launches_get_all_launches_error_404(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = NoDataFoundException

    response = mock_app.test_client().get("/launches/get_all_launches")

    assert response.status_code == 404
    assert response.json == "Request returned no results"


def test_launches_get_all_launches_unknown_exception(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = Exception

    response = mock_app.test_client().get("/launches/get_all_launches")

    assert response.status_code == 500
    assert (
        response.json
        == "Unknown error occurred, please contact API developers for assistance"
    )


def test_launches_get_all_launches_unknown_http_exception(mock_app):
    mock_app.spacex_api.get_all_launches.side_effect = Unauthorized

    response = mock_app.test_client().get("/launches/get_all_launches")

    assert response.status_code == 401
    assert (
        response.json["description"]
        == "The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
    )
    assert response.json["name"] == "Unauthorized"


# TODO Test get_all_launchpads_with_launches
