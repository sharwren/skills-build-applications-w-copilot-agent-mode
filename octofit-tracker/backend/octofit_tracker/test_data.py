from bson import ObjectId
from datetime import timedelta

def get_test_data():
    return {
        "users": [
            {"_id": ObjectId(), "username": "john_doe", "email": "john_doe@example.com", "password": "password123"},
            {"_id": ObjectId(), "username": "jane_smith", "email": "jane_smith@example.com", "password": "password123"},
            {"_id": ObjectId(), "username": "alice_jones", "email": "alice_jones@example.com", "password": "password123"},
        ],
        "teams": [
            {"_id": ObjectId(), "name": "Team Alpha", "members": ["john_doe", "jane_smith"]},
            {"_id": ObjectId(), "name": "Team Beta", "members": ["alice_jones"]},
        ],
        "activities": [
            {"_id": ObjectId(), "user": "john_doe", "activity_type": "Running", "duration": timedelta(minutes=30)},
            {"_id": ObjectId(), "user": "jane_smith", "activity_type": "Cycling", "duration": timedelta(minutes=45)},
            {"_id": ObjectId(), "user": "alice_jones", "activity_type": "Swimming", "duration": timedelta(minutes=60)},
        ],
        "leaderboard": [
            {"_id": ObjectId(), "user": "john_doe", "score": 100},
            {"_id": ObjectId(), "user": "jane_smith", "score": 90},
            {"_id": ObjectId(), "user": "alice_jones", "score": 80},
        ],
        "workouts": [
            {"_id": ObjectId(), "name": "Morning Run", "description": "A 5km run to start the day"},
            {"_id": ObjectId(), "name": "Evening Cycle", "description": "A 10km cycling session"},
            {"_id": ObjectId(), "name": "Swimming Laps", "description": "30 minutes of swimming laps"},
        ],
    }