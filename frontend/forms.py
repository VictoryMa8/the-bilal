from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

# Django doesn't want to assume how we want our sign up form to be
# Thus, we have to declare it manually
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]