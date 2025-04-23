from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.exceptions import ObjectDoesNotExist



# @method_decorator(csrf_exempt,name='dispatch')
class AllTransactionHistory(View):
    def get(self, request):
            user_id = request.session.get('user_id')
            try:
                user = User.objects.get(id=user_id)
            except ObjectDoesNotExist:
                return render(request, 'login.html')

            # Fetch categories and payment methods from the database
            categories = IncomeCategory.objects.all()
            payment_methods = PaymentMethod.objects.all()

            # Get transaction_type from the GET parameters
            transaction_type = request.GET.get('type', 'all')  # Default to 'all' if no type is provided

            user_seen = User.objects.get(id=user_id)

            # Fetching income and expense data for the user
            fetch_income = Income.objects.filter(user_id=user_seen)
            fetch_expense = Expense.objects.filter(user_id=user_seen)

            # Initialize an empty list to hold the transactions
            transactions_list = []

            for income in fetch_income:
                data = {
                    'type': 'income',
                    'category_name': income.category,
                    'description': income.description,
                    'amount': income.amount,
                    'payment_method': income.payment_method,
                    'date': income.date
                }
                transactions_list.append(data)

            for expense in fetch_expense:
                data = {
                    'type': 'expense',
                    'category_name': expense.category,
                    'description': expense.description,
                    'amount': expense.amount,
                    'payment_method': expense.payment_method,
                    'date': expense.date
                }
                transactions_list.append(data)

            # Render the template with the transaction data
            return render(request, 'transaction_history.html', {
                'transactions': transactions_list,
                'categories': categories,
                'payment_methods': payment_methods,
            })
    


    def post(self, request):
        user_id = request.session.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return render(request, 'login.html')

        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        else:
            data = request.POST

            transaction_type = data.get('type')
            category_id = data.get('category')
            payment_method_id = data.get('payment_method')
            date_filter = data.get('date-filter')

            # Fetch categories and payment methods from the database
            categories = IncomeCategory.objects.all()
            payment_methods = PaymentMethod.objects.all()


            user_seen = User.objects.get(id=user_id)
            fetch_income = Income.objects.filter(user_id=user_seen)
            fetch_expense = Expense.objects.filter(user_id=user_seen)


            transactions_list = []
            if transaction_type == 'income':
                for income in fetch_income:
                        data = {
                            'type':'income',
                            'category_name': income.category,
                            'description':income.description,
                            'amount': income.amount,
                            'payment_method':income.payment_method,
                            'date': income.date
                        }
                        transactions_list.append(data)

            elif transaction_type == 'expense':
                for expense in fetch_expense:
                        data = {
                            'type':'expense',
                            'category_name': expense.category,
                            'description':expense.description,
                            'amount': expense.amount,
                            'payment_method':expense.payment_method,
                            'date': expense.date
                        }
                        
                        transactions_list.append(data)

            
            return render(request, 'transaction_history.html', {
                            'transactions': transactions_list,
                            'categories': categories,
                            'payment_methods': payment_methods
                        })
        