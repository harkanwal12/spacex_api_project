from api.classes.spacex import SpaceX
from api import create_app
from flask import Flask


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
