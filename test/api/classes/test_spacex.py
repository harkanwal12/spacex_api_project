from api.classes.spacex import SpaceX
from api.classes.connection import SpacexConnection
from api.classes.entities import Launch, Launchpad


def test_spacex_constructor(mocker, mock_connection):
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    assert isinstance(spacex._conn, SpacexConnection)
    mock_conn.assert_called_with("https://api.spacexdata.com", True, None)


def test_spacex_constructor_with_arguments(
    mocker, mock_connection, mock_logger
):
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX("someurl", False, mock_logger)
    assert isinstance(spacex._conn, SpacexConnection)
    mock_conn.assert_called_with("someurl", False, mock_logger)


def test_spacex_get_all_launches_success(
    mocker, mock_connection, example_launch_json
):

    mock_connection.get.return_value = [
        example_launch_json,
        example_launch_json,
    ]
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    launch_list = spacex.get_all_launches()

    assert all(isinstance(launch, Launch) for launch in launch_list)
    mock_connection.get.assert_called_with("/v4/launches")
    assert len(launch_list) == 2


def test_spacex_get_all_launchepads_success(
    mocker, mock_connection, example_launchpad_json
):

    mock_connection.get.return_value = [
        example_launchpad_json,
        example_launchpad_json,
    ]
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    launchpad_list = spacex.get_all_launchpads()

    assert all(
        isinstance(launchpad, Launchpad) for launchpad in launchpad_list
    )
    mock_connection.get.assert_called_with("/v4/launchpads")
    assert len(launchpad_list) == 2
