from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(_id=ObjectId(), username='testuser', email='testuser@example.com', password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(_id=ObjectId(), username='teamuser', email='teamuser@example.com', password='password123')
        team = Team.objects.create(_id=ObjectId(), name='Team Test')
        team.members.add(user)
        self.assertEqual(team.name, 'Team Test')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(_id=ObjectId(), username='activityuser', email='activityuser@example.com', password='password123')
        activity = Activity.objects.create(_id=ObjectId(), user=user, activity_type='Running', duration=timedelta(minutes=30))
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(activity.duration, timedelta(minutes=30))

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(_id=ObjectId(), username='leaderboarduser', email='leaderboarduser@example.com', password='password123')
        leaderboard = Leaderboard.objects.create(_id=ObjectId(), user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(_id=ObjectId(), name='Morning Run', description='A 5km run to start the day')
        self.assertEqual(workout.name, 'Morning Run')
        self.assertEqual(workout.description, 'A 5km run to start the day')