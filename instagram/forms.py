from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class UserForm(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 270px;'}),max_length=30)
  last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 270px;'}),max_length=30)
  email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'style': 'width: 270px;'}))
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 270px;'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 270px;'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 270px;'}))
  class Meta:
    model = User
    fields = ['email','username','first_name','last_name','password1','password2']
    
class LoginForm(AuthenticationForm): 
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
  class Meta:
    model = User
    fields = ['username','password']
    
    
class PostImageForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 200px;'}))
  caption = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Caption', 'style': 'width: 200px; margin-top:20px'}))
  image = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Caption', 'style': 'width: 200px; margin-top:20px'}))
  class Meta:
    model = Image
    fields = ['image','caption','name']

