import pytest

def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all activities with correct structure."""
    # Arrange - client fixture provides TestClient

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert len(activities) == 9  # All activities present

def test_get_activities_structure(client):
    """Test that each activity has the required fields."""
    # Arrange - client fixture provides TestClient

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()

    for activity_name, activity_data in activities.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)

def test_get_activities_participant_counts(client):
    """Test that participant counts are accurate."""
    # Arrange - client fixture provides TestClient

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()

    # Check specific activities with known participant counts
    assert len(activities["Chess Club"]["participants"]) == 2
    assert len(activities["Programming Class"]["participants"]) == 2
    assert len(activities["Gym Class"]["participants"]) == 2
    assert len(activities["Basketball Team"]["participants"]) == 0