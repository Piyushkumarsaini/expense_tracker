from django.shortcuts import render, redirect
from django.http import JsonResponse
from user.models import User
from transaction.models import Income, Expense
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Sum
from datetime import date
from itertools import chain

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
          
          income_today = Income.objects.filter(user_id=user_seen, date=today).order_by('-id')[:5]
          expense_today = Expense.objects.filter(user_id=user_seen, date=today).order_by('-id')[:5]

          combineds = list(chain(income_today,expense_today))


          transactions_list = []

          for combined in combineds:
               transactions_list.append({
                    'type':combined.type,
                    'category_name': combined.category,
                    'description':combined.description,
                    'amount': combined.amount,
                    'payment_method':combined.payment_method,
                    'date': combined.date
               })
          # for expense in expense_today:
          #      transactions_list.append({
          #           'type':'expense',
          #           'category_name': expense.category,
          #           'description':expense.description,
          #           'amount': expense.amount,
          #           'payment_method':expense.payment_method,
          #           'date': expense.date
          #      })

          return render(request, 'dashboard.html',{
               'transactions':transactions_list,
               'total_income': total_income,
               'total_expense':total_expense,
               'total':total
          })
     