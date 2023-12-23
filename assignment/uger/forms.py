from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']


class ProfileUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        
