from django.shortcuts import render, redirect
from django.http import JsonResponse
from transaction.models import Income, Expense
from categories.models import Category
from payment.models import PaymentMethod
from user.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist

class AddTransaction(View):
    def get(self, request):
        user_id = request.session.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return render(request, 'login.html')

        total_income_data = Income.objects.filter(user_id=user).aggregate(total_income=Sum('amount'))
        total_expense_data = Expense.objects.filter(user_id=user).aggregate(total_expense=Sum('amount'))

        total_expense = total_expense_data['total_expense'] or 0
        total_income = total_income_data['total_income'] or 0
        total = total_expense + total_income

        # Fetch categories and payment methods from the database
        categories = Category.objects.all()
        print(categories)
        # payment_methods = UserPaymentMethod.objects.all()

        # All available payment methods
        all_payment_methods = PaymentMethod.objects.all()

        assigned_methods = PaymentMethod.objects.filter(user=user).values_list('id', flat=True)

        return render(request, 'transaction.html', {
            'categories': categories,
            'payment_methods': all_payment_methods,
            'assigned_methods': list(assigned_methods),   
            'total_income': total_income,
            'total_expense': total_expense,
            'total': total,
        })

    def post(self, request):
        user_id = request.session.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        else:
            data = request.POST

        # Validate and convert data
        transaction_type = data.get('type')
        category_id = data.get('category')
        payment_method_id = data.get('payment_method')
        amount = data.get('amount')
        description = data.get('description', '')

        if not all([transaction_type, category_id, payment_method_id, amount]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            fetch_category = Income.objects.get(id=category_id)
            fetch_payment = PaymentMethod.objects.get(id=payment_method_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Invalid category or payment method'}, status=400)

        if transaction_type == 'income':
            save_income_datiles = Income.objects.create(
                user_id=user,
                type=transaction_type,
                category=fetch_category,
                payment_method=fetch_payment,
                amount=amount,
                description=description
                )
            
            save_income_datiles.save()

        elif transaction_type == 'expense':
            save_expense_details = Expense.objects.create(
                user_id=user,
                type=transaction_type,
                category=fetch_category,
                payment_method=fetch_payment,
                amount=amount,
                description=description
                )
            print(save_expense_details)
            save_expense_details.save()

        else:
            return JsonResponse({'error': 'Invalid transaction type'}, status=400)

        # Fetch updated categories and payment methods for the template
        categories = Income.objects.all()
        payment_methods = PaymentMethod.objects.all()
        total_income_data = Income.objects.filter(user_id=user).aggregate(total_income=Sum('amount'))
        total_expense_data = Expense.objects.filter(user_id=user).aggregate(total_expense=Sum('amount'))
        total_expense = total_expense_data['total_expense'] or 0
        total_income = total_income_data['total_income'] or 0
        total = total_expense + total_income

        return render(request, 'transaction_add.html', {
            'categories': categories,
            'payment_methods': payment_methods,
            'total_income': total_income,
            'total_expense': total_expense,
            'total': total,
            'success_message': 'Transaction added successfully!'  # Optional success feedback
        })

# # Helper function to get CSRF token (if needed for AJAX)
# def get_cookie(request, cookie_name):
#     return request.COOKIES.get(cookie_name)