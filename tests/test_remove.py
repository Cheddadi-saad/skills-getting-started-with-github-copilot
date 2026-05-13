import pytest

def test_remove_participant_successful(client):
    """Test successful removal of a participant from an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Removed {email} from {activity_name}" in data["message"]

    # Verify participant was removed
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email not in activities[activity_name]["participants"]

def test_remove_activity_not_found(client):
    """Test removal fails for non-existent activity."""
    # Arrange
    invalid_activity = "NonExistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{invalid_activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]

def test_remove_student_not_signed_up(client):
    """Test removal fails when student is not signed up for the activity."""
    # Arrange
    activity_name = "Basketball Team"
    email = "notsignedup@mergington.edu"  # Not signed up

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "Student is not signed up for this activity" in data["detail"]