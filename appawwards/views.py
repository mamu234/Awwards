from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


from django.shortcuts import render
from .models import Post 

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})