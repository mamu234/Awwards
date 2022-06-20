from django.shortcuts import render
from django.http import HttpResponse



tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def index(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/index.html",context)

def about(request):
    return HttpResponse('<h1>About</h1>')

posts = [
    {
        'author': 'Anna',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'August 10, 2020'
    },
    {
        'author': 'Jane',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'August 1, 2020'
    }
]

