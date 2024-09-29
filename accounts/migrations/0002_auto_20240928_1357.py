from django.db import models
from django.db import migrations

def populate_role(apps, schemaeditor):
    entries = {
        "developer": "The person who works on issues",
        "scrum master": "The team's coach",
        "product owner": "Responsible for issue creation"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

def populate_team(apps, schemaeditor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.CharField(max_length=256),
        ),
        # Other operations
    ]
