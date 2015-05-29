from django.contrib.auth import forms as authforms
from users.models import User


class RegistrationForm(authforms.UserCreationForm):
    class Meta(authforms.UserCreationForm.Meta):
        model = User
