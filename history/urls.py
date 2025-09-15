from django.contrib import admin
from django.urls import path,include
from history.views import AllTransactionHistory

urlpatterns = [
    path('', AllTransactionHistory.as_view(), name='transaction_history'),
]
