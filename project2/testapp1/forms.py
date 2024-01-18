from django import forms
from .models import StudentsModel
from django.contrib.auth.models import User

class StudentsForm(forms.ModelForm):
    class Meta:
        model=StudentsModel
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']