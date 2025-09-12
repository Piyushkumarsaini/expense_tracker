from django.urls import path,include
from . import views
from .view.signup import *
from .view.login import *
from .view.forgottpassword import *
# from .view.categories import *
# from .view.payment_method import *
from .view.dashboard import *
from .view.all_transaction_history import *
from .view.transactionadd import *


urlpatterns = [
    # path('signup/',Signup.as_view(), name='signup'),
    path('login/',Login.as_view(), name='login'),
    path('verify_email/',VerifyEmail.as_view(), name='verify_email'),
    path('reset_password/',SetNewPassword.as_view(), name='reset_password'),
    path('dashboard/',DashBoard.as_view(), name='dashboard'),
    path('transaction_history/',AllTransactionHistory.as_view(), name='transaction_history'),
    path('add_transaction/',AddTransaction.as_view(), name='add_transaction'),
    # path('aaa/',views.aaaaaaaa,name='aa'),




    # path('income/<int:user_id>/',AddIncome.as_view(), name='income_add'),
    # path('income/sdfdf',IncomeDetail.as_view(), name='show_income'),
    # path('income/<int:user_id>/delete/<int:income_id>', IncomeDetail.as_view(), name='income_delete'),
    # path('income/<int:user_id>/update/<int:income_id>', IncomeDetail.as_view(), name='income_update'),
    # path('expense/',AddExpense.as_view(), name='expense_add'),
    # path('expense/<int:user_id>',ExpenseDetail.as_view(), name='expense_show'),
    # path('expense/<int:user_id>/delete/<int:expense_id>', ExpenseDetail.as_view(), name='expense_delete'),
    # path('expense/<int:user_id>/update/<int:expense_id>', ExpenseDetail.as_view(), name='expense_update'),
    # path('total/<int:user_id>',Total.as_view(), name='expense_add'),
    # path('tom/',PaymentMethodDetileAdd.as_view(), name='expense_add'),
    # path('',views.tom1)

]
