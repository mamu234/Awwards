from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt





urlpatterns = [
    path("", views.home, name="home"),
    path('register',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]

