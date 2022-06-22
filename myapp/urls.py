from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.home, name='home'),
    path('update/<int:post_id>',views.update_post,name='update'),
    path('delete/<int:post_id>',views.delete_post,name='delete'),
    path('register',(views.register), name="register"),
    path('login/',(auth_views.LoginView.as_view(template_name='login.html')), name='login'),
   
]