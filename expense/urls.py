from django.urls import path,include
from .view.signup import *
from .view.login import *
from .view.income import *
from .view.expense import *
# from .view.expensecategory import *
# from .view.incomecategory import *
# from .view.payment_method import *
from .view.changepassword import *
from .view.totale import *


urlpatterns = [
    path('signup/',Signup.as_view(), name='signup'),
    path('changepassword/',ChangePassword.as_view(), name='change_password'),
    path('login/',Login.as_view(), name='login'),
    path('income/',IncomeDetail.as_view(), name='income_add'),
    path('income/<int:user_id>',IncomeDetail.as_view(), name='show_income'),
    path('income/<int:user_id>/delete/<int:income_id>', IncomeDetail.as_view(), name='income_delete'),
    path('income/<int:user_id>/update/<int:income_id>', IncomeDetail.as_view(), name='income_update'),
    path('expense/',ExpenseDetail.as_view(), name='expense_add'),
    path('expense/<int:user_id>',ExpenseDetail.as_view(), name='expense_show'),
    path('expense/<int:user_id>/delete/<int:expense_id>', ExpenseDetail.as_view(), name='expense_delete'),
    path('expense/<int:user_id>/update/<int:expense_id>', ExpenseDetail.as_view(), name='expense_update'),
    path('total/<int:user_id>',Totale.as_view(), name='expense_add'),

]
