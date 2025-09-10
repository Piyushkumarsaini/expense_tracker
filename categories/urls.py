from django.urls import path
from .views import CategoriesShow, CategoriesEdit, CategoriesDelete

urlpatterns = [
    path('', CategoriesShow.as_view(), name='category_show'),
    # path('add/', CategoriesAdd.as_view(), name='category_add'),
    path('edit/<int:category_id>/', CategoriesEdit.as_view(), name='categories_edit'),
    path('delete/<int:category_id>/', CategoriesDelete.as_view(), name='categories_delete'),
]
