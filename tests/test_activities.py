from src.app import activities


def test_root_redirects_to_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert set(data) == set(activities)
    assert len(data) == 9


def test_get_activities_includes_expected_fields(client):
    data = client.get("/activities").json()

    for details in data.values():
        assert set(details) == {"description", "schedule", "max_participants", "participants"}
        assert isinstance(details["participants"], list)
