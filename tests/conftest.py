import pytest
from fastapi.testclient import TestClient
from src.app import app
import copy

# Initial activities data for state restoration
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice basketball skills and compete in games",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Soccer Club": {
        "description": "Train for soccer matches and improve teamwork",
        "schedule": "Mondays and Wednesdays, 3:00 PM - 4:30 PM",
        "max_participants": 22,
        "participants": []
    },
    "Art Club": {
        "description": "Explore various art forms and create masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Drama Club": {
        "description": "Act in plays and improve public speaking",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Debate Club": {
        "description": "Learn argumentation and debate topics",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and learn about science",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 18,
        "participants": []
    }
}

@pytest.fixture
def client():
    """Provides a TestClient instance for testing FastAPI endpoints."""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Resets the activities global state before each test."""
    from src.app import activities
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))