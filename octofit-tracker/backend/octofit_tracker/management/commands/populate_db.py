from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create(username='ironman', email='tony@stark.com', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create(username='captain', email='steve@rogers.com', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create(username='batman', email='bruce@wayne.com', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create(username='superman', email='clark@kent.com', first_name='Clark', last_name='Kent', team=dc)

        # Add members to teams
        marvel.members.add(tony, steve)
        dc.members.add(bruce, clark)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, calories=300, date='2023-01-01')
        Activity.objects.create(user=steve, type='walk', duration=60, calories=200, date='2023-01-02')
        Activity.objects.create(user=bruce, type='cycle', duration=45, calories=400, date='2023-01-03')
        Activity.objects.create(user=clark, type='swim', duration=50, calories=500, date='2023-01-04')

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='strength')
        Workout.objects.create(name='Jogging', description='Jog for 30 minutes', suggested_for='endurance')

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, score=500)
        Leaderboard.objects.create(team=dc, score=600)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))