from django.shortcuts import render,redirect
from .forms import *
from .forms import UserRegisterForm, UserCreationForm
from django.contrib import messages
from django.http import Http404, HttpResponse
from . models import Post, Profile,Rating
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "index.html")

def main_view(request):
    obj =Rating.objects.filter(score =1).order_by("?").first()
    context ={
        'object':obj
    }
    return render(request,'index.html',context)
    
   
    

# def register(request):
#     if request.method == 'POST':
#         form =UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f"You have succesfully created an account. Proceed to Login")
#             return redirect('login')



    # else:
    #     form = UserRegisterForm()
    # context = {
    #     'form':form
    # }
    # return render(request,"sign-up.html",context)
  
       
def upload(request):
    upload=UploadpostForm()
    if request.method=='POST':
        upload=UploadpostForm(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'upload.html',{'upload':upload})

def update(request,post_id):
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

def delete(request,blog_id):
    post_id=int(post_id)
    try:
        blog_up=Post.objects.get(id=blog_id)
    except Post.DoesNotExist:
        return redirect('index.html')
    blog_up.delete()
    return redirect('index.html')

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"registration/register.html",context)


def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadpostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = UploadpostForm()
    return render(request, 'new_post.html', { "form":form})

@login_required(login_url='registration/login/')
def vote(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        raise Http404()
    return render(request,"vote.html", {"post":post})

