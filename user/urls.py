from django.contrib import admin
from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('register/', views.Register , name = "register"),
    path('login/', views.Login , name = "login"),
    path('logout/', views.Logout , name = "logout"),
]

