from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Sum


@method_decorator(csrf_exempt,name='dispatch')
class Total(View):
    def get(self,request,user_id):
        try:
            user = User.objects.get(id=user_id)

            total_income_data = Income.objects.filter(user_id=user).aggregate(total_income=Sum('amount'))
            total_expense_data = Expense.objects.filter(user_id=user).aggregate(total_expense=Sum('amount'))


            total_income = total_income_data['total_income'] or 0
            total_expense = total_expense_data['total_expense'] or 0

            return JsonResponse({
                'user_id':user.id,
                'total_income': total_income,
                'total_expense':total_expense
                })
    
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)