from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt





urlpatterns = [
    path("", views.home, name="home"),
    path('register'),csrf_exempt(views.register,name='register'),
    path('login'),csrf_exempt(auth_views.LoginView.as_view(template_name='login.html', name='login')),
    path('logout'),csrf_exempt(auth_views.LoginView.as_view(template_name='logout.html', name='logout'))
]
