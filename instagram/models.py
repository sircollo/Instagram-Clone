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
    return f'{self.user.username} Profile'
  
  def save_profile(self):
    self.save()
  
  def delete_profile(self):
    self.delete()
  
  @classmethod
  def search_user(cls, name):
      return cls.objects.filter(user__username__icontains=name).all()
  

class Image(models.Model):
  image = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30,default='image_name')
  caption = models.CharField(max_length=30,default='')
  upload_date = models.DateTimeField(auto_now_add=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='image')
  likes = models.ManyToManyField(User, related_name='likes',blank=True)
  
  def __str__(self):
    return self.name
  
  def save_image(self):
    self.save()
    
  def delete_image(self):
    self.delete()
    
  

class Comment(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
  image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comments')

  def __str__(self):
    return self.comment

