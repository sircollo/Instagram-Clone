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
from django.views.generic import ListView,CreateView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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
  current_user = request.user
  get_profile = Profile.objects.filter(user=current_user.id).first()
  user = Image.objects.filter(user=get_profile).all()
  if request.method == 'POST':
      upload_form = PostImageForm(request.POST,request.FILES)
      if upload_form.is_valid():
          post = upload_form.save(commit=True)
          post.user= get_profile
          post.save()
          img = upload_form.cleaned_data['img']
          name = upload_form.cleaned_data['name']
          caption = upload_form.cleaned_data['caption']
          upload = Image(img=img, name=name,caption=caption, user=get_profile)
          upload.save_image()
          return redirect('index')
  else:
      upload_form =PostImageForm
  context = {'upload_form':upload_form,'users':users,'images':images,'comments':comments,"current":current_user}
  return render(request, 'home.html',context)


@login_required(login_url='/')
def postImage(request):
  upload_form =PostImageForm()
  user = Profile.objects.get(user=request.user)
  if request.method == 'POST':
    upload_form = PostImageForm(request.POST,request.FILES)
    if upload_form.is_valid():
      img = upload_form.cleaned_data['img']
      name = upload_form.cleaned_data['name']
      caption = upload_form.cleaned_data['caption']
      
      new_image = Image(img=img,name=name,caption=caption,user=user)
      new_image.save()
      return redirect('')
  else:
      upload_form =PostImageForm
  return render(request, 'home.html', {"upload_form": upload_form})





@login_required(login_url='/')
def comments(request,pk):
  # user = request.user
  image = Image.objects.get(id=pk)
  comments = Comment.objects.filter(image=image)
  if request.method == 'POST':
      comment = request.POST.get('comment')
      commentor = Profile.objects.get(user=request.user)
      new_comment = Comment.objects.create(comment=comment,image=image,user=commentor)
      new_comment.save()
    
  context = {'comment': comments, 'image':image} 
  return render(request, 'comments.html', context )



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
@login_required(login_url='/')
def updateProfile(request,id):
    profile = Profile.objects.get(user=id)
    form = UpdateProfileForm(request.POST, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'update_profile.html', context)
@login_required(login_url='/')  
def unfollow(request, pk):
  if request.method == 'GET':
      try:
          user1 = User.objects.get(username=pk)
      except User.DoesNotExist:
          user1 = None

      unfollow= Follow.objects.filter(follower=request.user, following=user1)
      unfollow.delete()
      return redirect('profile')

@login_required(login_url='/')
def follow(request, pk):
    if request.method == 'GET':
        try:
            user2 = User.objects.get(username=pk)
        except User.DoesNotExist:
            user2 = None
    follow = Follow(follower=request.user, following=user2)
    follow.save()
    
    return redirect('index')
    
      
      
@login_required(login_url='/')  
def like(request, pk):
  user = request.user
  image = Image.objects.get(id=pk)
  current_likes = image.likes
  liked = Like.objects.filter(user=user, image=image)
  
  if not liked:
    like = Like.objects.create(user=user, image=image)
    current_likes = current_likes + 1

  else:
    Like.objects.filter(user=user, image=image).delete()
    current_likes = current_likes - 1

  image.likes = current_likes
  image.save()

  return HttpResponseRedirect(reverse('index'))


class CreateProfilePageView(CreateView):
  model = Profile
  form_class = CreateProfileForm
  template_name = 'create_profile.html'
  # fields = ['photo','bio']
  
  
  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)
