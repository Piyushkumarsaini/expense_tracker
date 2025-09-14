from django.contrib import admin
from django.urls import path,include
from dashboard.views import DashBoard

urlpatterns = [
    path("", DashBoard.as_view(), name="dashboard")
]
