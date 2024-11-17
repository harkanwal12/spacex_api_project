from api.classes.connection import SpacexConnection
from api.classes.exceptions import NoDataFoundException, BadJSONException
from unittest.mock import patch, Mock
import logging
import requests
import pytest


def test_connection_construction_no_args(mock_logger, mocker):
    mocker.patch(
        "api.classes.connection.logging.getLogger",
        return_value=mock_logger,
    )

    conn = SpacexConnection()

    assert conn._base_url == "https://api.spacexdata.com"
    assert isinstance(conn._logger, logging.Logger)
    assert conn._ssl_verify


def test_connection_construction_with_args(mock_logger):
    conn = SpacexConnection("someurl", False, mock_logger)

    assert conn._base_url == "someurl"
    assert isinstance(conn._logger, logging.Logger)
    assert not conn._ssl_verify


def test_connection_get_success(mock_logger, mocker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    requests_mock = mocker.patch("requests.get", return_value=mock_response)

    conn = SpacexConnection("someurl/", False, mock_logger)

    response = conn.get("someendpoint")

    requests_mock.assert_called_with("someurl/someendpoint", verify=False)
    assert response == {"key": "value"}


def test_connection_get_404_error(mock_logger, mocker):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        response=mock_response
    )
    mocker.patch("requests.get", return_value=mock_response)

    conn = SpacexConnection("someurl/", False, mock_logger)

    with pytest.raises(NoDataFoundException) as err:
        conn.get("someendpoint")

    assert str(err.value) == "No data found for request"


def test_connection_get_any_error(mock_logger, mocker):
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        response=mock_response
    )
    mocker.patch("requests.get", return_value=mock_response)

    conn = SpacexConnection("someurl/", False, mock_logger)

    with pytest.raises(requests.exceptions.HTTPError) as err:
        conn.get("someendpoint")


def test_get_bad_json(mock_logger, mocker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError(
        "No JSON object could be decoded"
    )
    mocker.patch("requests.get", return_value=mock_response)

    conn = SpacexConnection("someurl/", False, mock_logger)

    with pytest.raises(BadJSONException) as err:
        conn.get("someendpoint")

    assert str(err.value) == "Bad JSON in response"
