from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True','class':'form-control'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput (attrs={'class ' : 'form-control'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput (attrs={'class ' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    

