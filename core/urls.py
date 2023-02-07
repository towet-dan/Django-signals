from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_view

urlpatterns = [
     path('home', views.home, name = 'home'),
     path('', views.register, name = 'register'),
     path('login/', auth_view.LoginView.as_view(template_name='login.html'), name = 'login' ),
     path('logout', auth_view.LogoutView.as_view(next_page = 'login'), name = 'logout')
]
