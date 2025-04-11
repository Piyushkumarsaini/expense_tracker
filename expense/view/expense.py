from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class ExpenseDetail(View):
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        user_id = data.get('id')
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status=400)

        category_id = data.get('category_id')
        if not category_id:
            return JsonResponse({'error': 'Category ID is required'}, status=400)

        payment_method_id = data.get('payment_method_id')
        if not payment_method_id:
            return JsonResponse({'error': 'Payment method ID is required'}, status=400)

        amount = data.get('amount')
        if not amount:
            return JsonResponse({'error': 'Amount is required'}, status=400)

        description = data.get('description')

        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_category = ExpenseCategory.objects.get(id=category_id)
            fetch_payment_method = PaymentMethod.objects.get(id=payment_method_id)

            Expense.objects.create(
                user_id=fetch_user,
                category_id=fetch_category,
                category = fetch_category.expense_category,
                payment_method_id=fetch_payment_method,
                payment_method=fetch_payment_method.payment_method,
                amount=amount,
                description=description
            )
            return JsonResponse({'message': 'Expense added successfully'}, status=201)

        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)

        except ExpenseCategory.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=400)

        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'Payment method does not exist'}, status=400)
        




    def get(self, request, user_id):
        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_expense = Expense.objects.filter(user_id=fetch_user)

            expense_list = []
            for expense in fetch_expense:
                expense_data = {
                'id': expense.id,
                'category_name': expense.category,
                'payment_method': expense.payment_method,
                'amount': expense.amount,
                'description': expense.description,
                'date': expense.date,
                'time': expense.time
                }
                expense_list.append(expense_data)
            
            return JsonResponse({'expense_details': expense_list})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)



    def delete(self, request, user_id, expense_id):
        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_expense = Expense.objects.get(id=expense_id, user_id=fetch_user)
            fetch_expense.delete()

            return JsonResponse({'message': 'Expense deleted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        except Expense.DoesNotExist:
            return JsonResponse({'error': 'Expense not found'}, status=400)




    def patch(self, request, user_id, expense_id):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        

        amount = data.get('amount')
        description = data.get('description')
        expense_category_id = data.get('expense_category_id')
        payment_method_id = data.get('payment_method_id')

        try:
            fetch_user = User.objects.get(id=user_id)
            fetch_expense = Expense.objects.get(id=expense_id, user_id=fetch_user)
            new_category = ExpenseCategory.objects.get(id=expense_category_id)
            new_payment_method = PaymentMethod.objects.get(id=payment_method_id)

            fetch_expense.amount = amount
            fetch_expense.description = description
            fetch_expense.category_id = new_category
            fetch_expense.payment_method_id = new_payment_method
            fetch_expense.category = new_category.expense_category
            fetch_expense.payment_method = new_payment_method.payment_method

            fetch_expense.save()

            return JsonResponse({'message': 'Expense updated successfully'}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)
        except Expense.DoesNotExist:
            return JsonResponse({'error': 'Expense not found'}, status=400)