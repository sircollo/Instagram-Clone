from django.test import TestCase
from .models import *
from django.contrib.auth.models import *
# Create your tests here.

class TestProfileCase(TestCase):
  def setUp(self):
    self.user = User(username='collo')
    self.user.save()
    
    self.profile = Profile(id=1, photo='test.jpg',bio='test stuff',user=self.user)
    
  def test_instance(self):
    self.assertTrue(self.profile,Profile)
    
  def test_save_method(self):
    self.profile.save_profile()
    new_object = Profile.objects.all()
    self.assertTrue(len(new_object)>0)
    
class TestImageCase(TestCase):
  def setUp(self):
    self.profile = Profile(id=1, photo='test.jpg',bio='test stuff')
    self.profile.save()
    
    self.image = Image(image='test.jpg',name='test_image',caption='test_caption',user=self.profile)
  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))
    
  def test_save_method(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)
    
  def test_delete_method(self):
    self.image.delete_image()
    new_object = Profile.objects.all()
    self.assertTrue(len(new_object)<0)