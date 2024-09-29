from django.db import models
from django.contrib.auth.models import AbstractUser  # Corrected import

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)  # Fixed 'mdoels' typo

    def __str__(self):
        return self.name

# Custom User Model
class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    team = models.ForeignKey(
        'Team',  # Reference the 'Team' model as a string because it's defined later
        on_delete=models.CASCADE,
        blank=True, null=True
    )

class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)  # Add this field

    def __str__(self):
        return self.name

