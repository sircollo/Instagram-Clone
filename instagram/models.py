from distutils.command.upload import upload
from django.db import models
from cloudinary.models import CloudinaryField
import datetime
from django.contrib.auth.models import User

class Image(models.Model):
  image = CloudinaryField('image')
  name = models.CharField(max_length=30,default='image_name')
  caption = models.CharField(max_length=30,default='')
  upload_date = models.DateTimeField(auto_now_add=True, null=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
  
  def __str__(self):
    return self.name




