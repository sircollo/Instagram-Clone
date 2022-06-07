from distutils.command.upload import upload
from django.db import models
from cloudinary.models import CloudinaryField
import datetime
from django.contrib.auth.models import User
class Profile(models.Model):
  photo = CloudinaryField('image')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
  
  def __str__(self):
    return self.user.username
  
  def save_profile(self):
    self.save()
    
    
  def update_profile(self):
    self.update()
    
  def delete_profile(self):
    self.delete()
  
  @classmethod
  def search_user(cls, name):
      return cls.objects.filter(user__username__icontains=name).all()
  

class Image(models.Model):
  img = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30,default='image_name')
  caption = models.CharField(max_length=30,default='')
  upload_date = models.DateTimeField(auto_now_add=True, null=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,related_name='image')
  likes = models.IntegerField(default=0)
  
  def __str__(self):
    return self.name
  
  def save_image(self):
    self.save()
    
  def delete_image(self):
    return self.delete()  

    
  def update_caption(self, pk):
    caption =self.objects.get(caption=pk)
    return caption.save()
    
    


class Comment(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='comments')
  image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comments',default='')

  def __str__(self):
    return self.comment

class Follow(models.Model):
  follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower',null=True)
  following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following',null=True)
  
  def follow_user(sender, instance, *args, **kwargs):
    follow = instance
    sender = follow.follower
    following = follow.following

  def unfollow_user(sender, instance, *args, **kwargs):
    follow = instance
    sender = follow.follower
    following = follow.following

class Like(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
  image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_like')

  def user_liked_post(sender, instance, *args, **kwargs):
      like = instance
      post = like.post
      sender = like.user

  def user_unlike_post(sender, instance, *args, **kwargs):
      like = instance
      post = like.post
      sender = like.user
      
