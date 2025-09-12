from django.contrib import admin
from django.urls import path,include
from login.views import Login

urlpatterns = [
    path("", Login.as_view(), name="login"),    
]
