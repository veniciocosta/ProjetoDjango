from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CrarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields= ('username', 'email', 'password1', 'password2')