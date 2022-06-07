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
  img = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Caption', 'style': 'width: 200px; margin-top:20px'}))
  class Meta:
    model = Image
    fields = ['img','caption','name']
    
class UpdateProfileForm(forms.ModelForm):
  photo =CloudinaryField()
  bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))  
  class Meta:
    model = Profile
    fields = ['photo','bio']
  
  
class UpdateUserForm(forms.ModelForm):
  username = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['username', 'email']
    
class CreateProfileForm(forms.ModelForm):
  bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
  class Meta:
      model = Profile
      fields = ['photo','bio']
      
     
  