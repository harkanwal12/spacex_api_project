def test_index_success(mock_app):
    response = mock_app.test_client().get("/")

    assert response.status_code == 200
    assert response.json == "Welcome to the SpaceX Python Wrapper API"
