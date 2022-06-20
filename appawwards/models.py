from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE) 

    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/images')
    bio = models.TextField(max_length=800,default="Welcome Me!")

    def __str__(self):
        return self.user