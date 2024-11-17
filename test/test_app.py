from api.classes.spacex import SpaceX
from flask import Flask


def test_app_init(mock_app):
    assert isinstance(mock_app, Flask)
    assert mock_app.config["TESTING"]
    assert isinstance(mock_app.spacex_api, SpaceX)
