from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models


class PatientSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("already exists, please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("address already exists, please use a different one.")
        return email

class PatientForm(forms.ModelForm):
    
    class Meta:
        model=models.Patient
        fields=['bloodgroup','address','mobile','profile_pic']
        
class PatientUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['bloodgroup', 'address', 'mobile', 'profile_pic']

