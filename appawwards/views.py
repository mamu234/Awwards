from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
    posts =Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Account created for {username}!') # Show sucess message when account is created
            return redirect('home') # Redirect user to Homepage
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})