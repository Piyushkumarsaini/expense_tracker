from django.urls import path
from .views import *

urlpatterns = [
    path('', PaymentShow.as_view(), name='payment_show'),
    # path('add/', CategoriesAdd.as_view(), name='category_add'),
    path('edit/<int:payment_id>/', UpdatePayment.as_view(), name='payment_edit'),
    path('delete/<int:payment_id>/', DeletePayment.as_view(), name='payment_delete'),
]
