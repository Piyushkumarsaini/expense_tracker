from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
import json
import re
from django.contrib.auth.hashers import make_password
     

#     def delete(self,request,user_id,income_id):
#         try:
#             fetch_user = User.objects.get(id=user_id)
#             fetch_income = Income.objects.get(id=income_id,user_id=fetch_user)
#             fetch_income.delete()

#             return JsonResponse({'message': 'Income deleted successfully'})
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User does not exist'}, status=400)
#         except Income.DoesNotExist:
#             return JsonResponse({'error': 'Income not found'}, status=400)



#     def patch(self, request, user_id,income_id):

#         try:
#             data = json.loads(request.body.decode('utf-8'))
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'invalid json data'}, status=400)

#         amount = data.get('amount')      
#         income_category_id = data.get('income_category_id')
   
        
#         try:
#             fetch_user = User.objects.get(id=user_id)
#             fetch_income = Income.objects.get(id=income_id,user_id=fetch_user)
#             new_category = IncomeCategory.objects.get(id=income_category_id)
            

#             # update_income_datiles = Income(
#             #     category_id=fetch_income,
#             #     amount=amount,
#             #     )
#             fetch_income.amount = amount
#             fetch_income.category_id = new_category
#             fetch_income.category = new_category.income_category

#             fetch_income.save()
#             return JsonResponse({'message': 'Income updated successfully'})
        
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User does not exist'}, status=400)
#         except Income.DoesNotExist:
#             return JsonResponse({'error': 'Income not found'}, status=400)
#         except IncomeCategory.DoesNotExist:
#             return JsonResponse({'error': 'Income category does not exist'}, status=400)
        