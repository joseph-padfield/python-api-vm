from app import app


def test_hello_greets_by_name():
    response = app.test_client().get("/api/hello?name=Jo")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Jo!"}

def test_hello_returns_400_for_blank_name():
    response = app.test_client().get("/api/hello?name=")

    assert response.status_code == 400
    assert response.get_json() == {"error": "The name query parameter is required."}

def test_hello_returns_400_for_no_name():
    response = app.test_client().get("/api/hello")

    assert response.status_code == 400
    assert response.get_json() == {"error": "The name query parameter is required."}