from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



@method_decorator(csrf_exempt,name='dispatch')
class IncomeDetail(View):
    def get(self, request, user_id):
        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_expense = Income.objects.filter(user_id=fetch_user)

            income_list = []
            for income in fetch_expense:
                income_data = {
                    'id': income.id,
                    'user_id': income.user_id.id,
                    'amount': income.amount,
                    'category': income.category,
                    'date': income.date,
                    'time': income.time
                }
                income_list.append(income_data)
            
            return JsonResponse({'expense_details': income_list})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        


    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        user_id = data.get('id')
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status=400)
        

        amount = data.get('amount')
        if not amount:
             return JsonResponse({'error': 'Amount is required'}, status=400)
        
        income_category = data.get('income_category')
        if not income_category:
            return JsonResponse({'error': 'Income Method is required'}, status= 400)
                
        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_category = IncomeCategory.objects.get(id=income_category)
        
            save_income_datiles = Income.objects.create(
                user_id=fetch_user,
                category_id=fetch_category,
                amount=amount,
                category=fetch_category.income_category
                )
            
            save_income_datiles.save()
            return JsonResponse({'message':'Income added succssfully'}, status=201)
 
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        except IncomeCategory.DoesNotExist:
            return JsonResponse({'error': 'Income category does not exist'}, status=400)
        

    def delete(self,request,user_id,income_id):
        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_income = Income.objects.get(id=income_id,user_id=fetch_user)
            fetch_income.delete()

            return JsonResponse({'message': 'Income deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        except Income.DoesNotExist:
            return JsonResponse({'error': 'Income not found'}, status=400)



    def patch(self, request, user_id,income_id):

        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'invalid json data'}, status=400)

        amount = data.get('amount')      
        income_category_id = data.get('income_category_id')
   
        
        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_income = Income.objects.get(id=income_id,user_id=fetch_user)
            new_category = IncomeCategory.objects.get(id=income_category_id)
            

            # update_income_datiles = Income(
            #     category_id=fetch_income,
            #     amount=amount,
            #     )
            fetch_income.amount = amount
            fetch_income.category_id = new_category
            fetch_income.category = new_category.income_category

            fetch_income.save()
            return JsonResponse({'message': 'Income updated successfully'})
        
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        except Income.DoesNotExist:
            return JsonResponse({'error': 'Income not found'}, status=400)
        except IncomeCategory.DoesNotExist:
            return JsonResponse({'error': 'Income category does not exist'}, status=400)
        