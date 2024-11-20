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

    mock_connection.get.return_value = example_launch_json
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    launch_list = spacex.get_launches()

    assert all(isinstance(launch, Launch) for launch in launch_list)
    mock_connection.get.assert_called_with("/v4/launches")
    assert len(launch_list) == 2
    mock_connection.post.assert_not_called()


def test_spacex_get_single_launch_success(
    mocker, mock_connection, example_launch_json
):

    mock_connection.get.return_value = example_launch_json[1]
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    launch = spacex.get_launches(launch_id="someid")

    assert isinstance(launch[0], Launch)
    mock_connection.get.assert_called_with("/v4/launches/someid")
    mock_connection.post.assert_not_called()


def test_spacex_get_launch_with_query_success(
    mocker, mock_connection, example_launch_json
):

    mock_connection.post.return_value = example_launch_json
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection
    query = {"somequery": "somequerycontents"}
    spacex = SpaceX()
    launch_list = spacex.get_launches(query=query)

    assert all(isinstance(launch, Launch) for launch in launch_list)
    mock_connection.post.assert_called_with("/v4/launches/query", data=query)
    mock_connection.get.assert_not_called()
    assert len(launch_list) == 2


def test_spacex_get_all_launchpads_success(
    mocker, mock_connection, example_launchpad_json
):

    mock_connection.get.return_value = example_launchpad_json
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    launchpad_list = spacex.get_launchpads()

    assert all(
        isinstance(launchpad, Launchpad) for launchpad in launchpad_list
    )
    mock_connection.get.assert_called_with("/v4/launchpads")
    mock_connection.post.assert_not_called()
    assert len(launchpad_list) == 2


def test_spacex_get_single_launchpad_success(
    mocker, mock_connection, example_launchpad_json
):

    mock_connection.get.return_value = example_launchpad_json[1]
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection

    spacex = SpaceX()
    launchpad = spacex.get_launchpads(launchpad_id="someid")

    assert isinstance(launchpad[0], Launchpad)
    mock_connection.get.assert_called_with("/v4/launchpads/someid")
    mock_connection.post.assert_not_called()


def test_spacex_get_launchpads_with_query_success(
    mocker, mock_connection, example_launchpad_json
):

    mock_connection.post.return_value = example_launchpad_json
    mock_conn = mocker.patch("api.classes.spacex.SpacexConnection")
    mock_conn.return_value = mock_connection
    query = {"somequery": "somequerycontents"}
    spacex = SpaceX()
    launchpad_list = spacex.get_launchpads(query=query)

    assert all(
        isinstance(launchpad, Launchpad) for launchpad in launchpad_list
    )
    mock_connection.post.assert_called_with("/v4/launchpads/query", data=query)
    mock_connection.get.assert_not_called()
    assert len(launchpad_list) == 2
