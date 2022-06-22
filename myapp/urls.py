from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers




urlpatterns = [
        path('',views.index, name="index"),
        path('register/',views.register,name="register"),
        path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
        path('profile/',views.profile,name='profile'),
        path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
        path('upload/',views.Upload_Project,name="upload_project"),
        
    

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)