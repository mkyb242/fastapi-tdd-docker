from app import main


def test_ping(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/docs")

    # Then
    assert response.status_code == 200
