from django.contrib import admin
from django.urls import path,include
from user.views import Signup

urlpatterns = [
    path("", Signup.as_view(), name="signup"),
]