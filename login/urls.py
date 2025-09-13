from django.contrib import admin
from django.urls import path,include
from login.views import Login

urlpatterns = [
    path("login/", Login.as_view(), name="userlogin"),    
]
