from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
        path('',views.home,name="home"),
        path('registration/',views.register, name="registration"),
        path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
        path('search/', views.search_results, name='search_results'),
        path('new_post$', views.new_post, name='new-post'),
        path('vote/(<post_id>', views.vote, name='vote'),    
        path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
        path('rating',views.main_view,name='main_view')
]
