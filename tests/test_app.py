from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    # Use a unique email to avoid duplicate registration
    import uuid
    email = f"testuser_{uuid.uuid4().hex[:8]}@mergington.edu"
    activity = "Chess Club"
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert "Signed up" in response.json().get("message", "")

    # Try duplicate signup
    response2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert response2.status_code == 400
    assert "already signed up" in response2.json().get("detail", "")
