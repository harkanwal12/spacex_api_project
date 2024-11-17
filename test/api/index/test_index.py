from unittest.mock import Mock


def test_index_success(mock_app):
    mock_send_static_file = Mock()
    mock_send_static_file.return_value = "Static file content"
    mock_app.send_static_file = mock_send_static_file
    response = mock_app.test_client().get("/")

    assert response.status_code == 200
    assert response.data.decode() == "Static file content"
    mock_send_static_file.assert_called_once_with("index.html")
