from src.app import activities


def test_signup_adds_participant(client):
    email = "new.student@mergington.edu"

    response = client.post("/activities/Basketball Team/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Basketball Team"}
    assert email in activities["Basketball Team"]["participants"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post("/activities/Unknown Club/signup", params={"email": "a@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_returns_400(client):
    existing = "michael@mergington.edu"

    response = client.post("/activities/Chess Club/signup", params={"email": existing})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
    assert activities["Chess Club"]["participants"].count(existing) == 1
