from email import message
from urllib import request
from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username,password=password)
    
    if user is not None:
      login(request,user)
      redirect('index')
    else:
      messages.info(request, 'Incorrect Username or password')

  context = {}
  return render(request, 'registration/login.html',context)

  

