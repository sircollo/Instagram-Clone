from email import message
from urllib import request
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.

def home(request):
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username,password=password)
      if user is not None:
        login(request, user)
        messages.info(request,'Success')
        return redirect('index')
      else:
        messages.error(request,'Invalid username or password')
        
    else:
      messages.error(request,'Invalid username or password')
  form = LoginForm()
  return render(request, 'registration/login.html', {'form': form})
  
def register(request):
  if request.method == "POST":
     form = UserForm(request.POST)
     if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account created Successfully for '+ user)
     
        return redirect('home')
     else:
      messages.warning(request, 'Invalid username or password')

  form = UserForm()
  return render(request=request, template_name='django_registration/registration_form.html', context={'form':form})

def logoutUser(request):
  logout(request)
  return redirect('index')


@login_required(login_url='/')
def index(request):
  users = User.objects.all()
  images = Image.objects.all()
  context = {}
  current_user = request.user
  get_profile = Profile.objects.filter(id=current_user.id).first()
  user = Image.objects.filter(user=get_profile).all()
  if request.method == 'POST':
      upload_form = PostImageForm(request.POST,request.FILES)
      if upload_form.is_valid():
          post = upload_form.save(commit=False)
          post.user= get_profile
          post.save()
          return redirect('index')
  else:
      upload_form =PostImageForm
  context = {'upload_form':upload_form,'users':users,'images':images}
  return render(request, 'home.html',context)


@login_required(login_url='/')
def postImage(request):
  current_user = request.user
  get_profile = Profile.objects.filter(id=current_user.id).first()
  user = Image.objects.filter(user=get_profile).all()
  if request.method == 'POST':
      upload_form = PostImageForm(request.POST,request.FILES)
      if upload_form.is_valid():
          post = upload_form.save(commit=False)
          post.user= get_profile
          post.save()
          return redirect('')
  else:
      upload_form =PostImageForm
  return render(request, 'home.html', {"upload_form": upload_form})




@login_required(login_url='/')
def profile(request,pk):
  profile = User.objects.get(pk=pk)  
  images = Image.objects.filter(user__pk=pk)
  context = {'profile':profile,'images':images,'images':images}
  return render(request, 'profile.html',context)
    

class search_user(ListView):
  model = User
  template_name = 'search_results.html'
  # queryset = User.objects.filter(username__icontains='collo')
  def get_queryset(self): # new
      query = self.request.GET.get('search_user')
      object_list = User.objects.filter(
        Q(username__icontains=query))
      return object_list
