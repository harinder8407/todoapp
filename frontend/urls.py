from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name="register"),
	path('', views.login_user, name="login_user"), 
    path('', views.list, name = 'home'),
]