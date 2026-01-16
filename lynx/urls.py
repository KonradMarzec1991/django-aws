from django.urls import path

from lynx import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile-management', views.profile_management, name='profile-management'),
]