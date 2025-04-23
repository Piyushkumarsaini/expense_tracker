from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain



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

            # Fetching income and expense data for the user
            fetch_income = Income.objects.filter(user_id=user).order_by('-id')
            fetch_expense = Expense.objects.filter(user_id=user).order_by('-id')

            combineds = list(chain(fetch_income,fetch_expense))


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

            fetch_income = Income.objects.filter(user_id=user).order_by('-id')
            fetch_expense = Expense.objects.filter(user_id=user).order_by('-id')

            # combineds = list(chain(fetch_income,fetch_expense))


            transactions_list = []
            if transaction_type == 'income':
                for income in fetch_income:
                        data = {
                            'type':income.type,
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
                            'type':expense.type,
                            'category_name': expense.category,
                            'description':expense.description,
                            'amount': expense.amount,
                            'payment_method':expense.payment_method,
                            'date': expense.date
                        }
                        
                        transactions_list.append(data)
            
            
            # elif transaction_type == 'all':
            #     for combined in combineds:
            #         transactions_list.append({
            #                 'type':combined.type,
            #                 'category_name': combined.category,
            #                 'description':combined.description,
            #                 'amount': combined.amount,
            #                 'payment_method':combined.payment_method,
            #                 'date': combined.date
            #         })

            return render(request, 'transaction_history.html', {
                            'transactions': transactions_list,
                            'categories': categories,
                            'payment_methods': payment_methods
                        })
        