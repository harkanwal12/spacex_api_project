from api.classes.spacex import SpaceX
from api import create_app
from flask import Flask
from unittest.mock import Mock


def test_create_app_factory_testing(mock_app):
    assert isinstance(mock_app, Flask)
    assert mock_app.config["TESTING"]
    assert isinstance(mock_app.spacex_api, SpaceX)


def test_create_app_factory_default(mocker, mock_spacex):
    mocker.patch("api.dictConfig")
    mock_spacex_class = mocker.patch("api.SpaceX")
    mock_spacex_class.return_value = mock_spacex
    app = create_app()

    assert isinstance(app, Flask)
    assert isinstance(app.spacex_api, SpaceX)


def test_app(mocker, mock_app):
    mocker.patch("api.create_app", return_value=mock_app)
    from api.app import app

    assert isinstance(app, Flask)


def test_index_prod_success(mock_app, mocker):
    """This test validates that the front-end is served when navigating to
    the root endpoint of the flask app
    """
    mock_app.config["FRONTEND_BUILD_DIR"] = "somedir"
    mock_app.config["FRONTEND_ROOT_FILE"] = "somefile"
    mock_flask = mocker.patch("api.send_from_directory")
    mock_flask.return_value = "something"
    response = mock_app.test_client().get("/")

    assert response.status_code == 200
    assert response.data.decode() == "something"
    mock_flask.assert_called_with("somedir", "somefile")


def test_index_not_prod_success(mock_app, mocker):
    """This test validates that when not in production, routing defaults to
    the flask API
    """
    mock_app.config["FRONTEND_BUILD_DIR"] = None
    mock_app.config["FRONTEND_ROOT_FILE"] = "somefile"
    mock_flask = mocker.patch("api.send_from_directory")
    mock_flask.return_value = "something"
    response = mock_app.test_client().get("/")

    assert response.status_code == 302
    assert response.location == "/api/"
    assert (
        b"You should be redirected automatically to the target URL"
        in response.data
    )
    mock_flask.assert_not_called()


def test_prod_invalid_route_sent_to_frontend(mock_app, mocker):
    """This test validates that any 404 errors resulting from invalid routes
    get sent to the front-end to handle
    """
    mock_app.config["FRONTEND_BUILD_DIR"] = "somedir"
    mock_app.config["FRONTEND_ROOT_FILE"] = "somefile"
    mock_flask = mocker.patch("api.send_from_directory")
    mock_flask.return_value = "something"
    response = mock_app.test_client().get("/someinvalidroute")

    assert response.status_code == 200
    assert response.data.decode() == "something"
    mock_flask.assert_called_with("somedir", "somefile")


def test_index_not_prod_invalid_route(mock_app, mocker):
    """This test validates that when not in production, invalid routes are
    handled by flask
    """
    mock_app.config["FRONTEND_BUILD_DIR"] = None
    mock_app.config["FRONTEND_ROOT_FILE"] = "somefile"
    mock_flask = mocker.patch("api.send_from_directory")
    mock_flask.return_value = "something"
    response = mock_app.test_client().get("/some invalid route")

    assert response.status_code == 404
    assert response.json == "Resource is invalid or unavailable"
    mock_flask.assert_not_called()
