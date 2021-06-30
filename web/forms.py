from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
from django import forms

class addcus(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' ,'password1', 'password2']

