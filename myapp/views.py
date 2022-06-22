from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserCreationForm
from django.http import HttpRequest, HttpResponse

@login_required(login_url=('login'))
def home(request):
    posts =Post.objects.all()
    return render(request,'index.html',{'posts':posts})

@login_required(login_url=('login'))
def upload(request):
    upload=UserCreationForm()
    if request.method=='POST':
        upload=UserCreationForm(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'upload_form.html',{'upload':upload})
    

def update_post(request,post_id):
    post_id=int(post_id)
    try:
     blog_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('home')
    post_form=UserCreationForm(request.POST or None,instance=blog_up)
    if post_form.is_valid():
        post_form.save()
        return redirect('home')
    return render (request,'upload_form.html',{'upload':post_form})

def delete_post(request,blog_id):
     
    post_id=int(post_id)
    try:
        blog_up=Post.objects.get(id=blog_id)
    except Post.DoesNotExist:
        return redirect('index.html')
    blog_up.delete()
    return redirect('index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Your account has been created! You are now able to log in') # Show sucess message when account is created
            return redirect('login') # Redirect user to Login page
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form': form})



