from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm

)
from .models import CustomUser

class CustomUserCreationFor(UserCreationForm):
    class Meta(UserChangeForm):
        model = CustomUser 
        fields = UserChangeForm.Meta.fields
        