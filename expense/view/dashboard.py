from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Sum
from datetime import date

class DashBoard(View):
     def get(self,request):
          user_id = request.session.get('user_id')
          today = date.today()
          if not user_id:
               return render(request, 'login.html')
          
          user_seen = User.objects.get(id=user_id)

          total_income_data = Income.objects.filter(user_id=user_seen).aggregate(total_income=Sum('amount'))
          total_expense_data = Expense.objects.filter(user_id=user_seen).aggregate(total_expense=Sum('amount'))

          total_expense = total_expense_data['total_expense'] or 0
          total_income = total_income_data['total_income'] or 0


          total = total_expense + total_income
          
          income_today = Income.objects.filter(user_id=user_seen)[:5]
          expense_today = Expense.objects.filter(user_id=user_seen)[:5]


          transactions_list = []

          for income in income_today:
               transactions_list.append({
                    'type':'income',
                    'category_name': income.category,
                    'description':income.description,
                    'amount': income.amount,
                    'payment_method':income.payment_method,
                    'date': income.date
               })
          for expense in expense_today:
               transactions_list.append({
                    'type':'expense',
                    'category_name': expense.category,
                    'description':expense.description,
                    'amount': expense.amount,
                    'payment_method':expense.payment_method,
                    'date': expense.date
               })

          return render(request, 'dashboard.html',{
               'transactions':transactions_list,
               'total_income': total_income,
               'total_expense':total_expense,
               'total':total
          })
     