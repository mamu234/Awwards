# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# from django.db.models.signals import post_save,post_delete
# from django.dispatch import receiver
# import datetime as dt

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30, blank=True)
#     first_name=models.CharField(max_length=300,null=True)
#     last_name=models.CharField(max_length=300,null=True)
#     # date_joined = models.DateTimeField(defualt=timezone.now)
#     prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
#     bio = models.CharField(max_length=800,default="Welcome Me!")


#     @receiver(post_save, sender=User)
#     def create_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_profile(sender, instance, created, **kwargs):
#         instance.profile.save()
    
#     def __str__(self):
#         return f'{self.name} Profile'
    

# class Post(models.Model):
#     title = models.CharField(max_length=300,null=True)
#     description=models.CharField(max_length=800)
#     image = models.FileField(upload_to='posts/')
#     country = models.CharField(max_length=50)


# class Tag(models.Model):
#     name= models.CharField(max_length=100,blank=True)
#     description=models.TextField(blank=True)
    
#     def __str__(self):
#         return f'{self.name} Tag'

# class Comment(models.Model):
#     content=models.TextField(max_length=344)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
    bio = models.CharField(max_length=800,default="Welcome Me!")


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()

class Post(models.Model):
    sitename=models.CharField(max_length=50,null=True)
    url = models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=800,default=True)
    image = models.FileField(upload_to='posts/')
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posted_by",default=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ["-pk"]