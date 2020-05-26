from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MovieNames
from django import forms


class Searchform(forms.ModelForm):
    search=forms.CharField(label="Search", max_length=100)


    class Meta:
        model = MovieNames
        fields = ['search',]

class CreateUserForm(UserCreationForm):
     class Meta:
         model = User
         fields= ['first_name','last_name','username','email','password1','password2']
