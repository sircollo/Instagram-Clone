from email import message
from multiprocessing import context
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


# def index(request):
#   user = request.user
#   posts = Image.objects.filter(user=user)
#   group_ids = []
#   for post in posts:
#     group_ids.append(post.post_id)
#   post_items = Image.objects.filter(id__in=group_ids).all().order_by('-upload_date')
#   context = {
#     'post_items': post_items
#   }
#   return render(request, 'home.html',context)

@login_required(login_url='/')
def index(request):
  users = User.objects.all()
  images = Image.objects.all()
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
def postImage(request,id):
  user = request.user
  get_profile = Profile.objects.filter(id=user).first()
  images = Image.objects.filter(user=get_profile).all()
  if request.method == 'POST':
      upload_form = PostImageForm(request.POST,request.FILES)
      if upload_form.is_valid():
          post = upload_form.save(commit=False)
          post.user.username = get_profile
          post.save()
          return redirect('')
  else:
      upload_form =PostImageForm
  return render(request, 'home.html', {"upload_form": upload_form})




@login_required(login_url='/')
def profile(request,id):
  user=request.user
  profiles = Profile.objects.get(user=id)  
  images = Image.objects.filter(user=profiles)
  context = {'user':user,'images':images,'profiles':profiles}
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
