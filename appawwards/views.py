from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from .forms import UserRegisterForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import json
from django.http import JsonResponse
from django.core.mail import EmailMessage

# Create your views here.
@login_required
def home(request):
    posts =Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def upload(request):
    upload=UserCreationForm()
    if request.method=='POST':
        upload=UserCreationForm(request.POST,request.FILES)
        if upload.is_valid:
            upload.save()
            return redirect('home')
        else:
            return HttpResponse('your form is wrong')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            emailval=form.clean_data.get('email')
            form.save() # Save user to Database
            username = form.clean_data.get('username') # Get the username that is submitted
            domain = get_current_site(request).domain
            link=reverse('home')
            homepage_url= 'http://'+domain+link
            email=EmailMessage(
                f'Hi{username},welcome',
                f'sart you voting {homepage_url}'
            )
       