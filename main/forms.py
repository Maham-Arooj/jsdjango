"""
from django import forms
from .models import Item

class AddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('created_by',
        'title', 'image', 'description', 'price', 'pieces', 'labels', 'slug')
        """
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
class edituserprofile(UserChangeForm):
    password= None
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels= {'email': 'Email'}