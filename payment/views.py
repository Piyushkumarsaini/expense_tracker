from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import PaymentMethod
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



@method_decorator(csrf_exempt,name='dispatch')
class PaymentShow(View):
    def get(self,request):
        try:
            fatch_category = PaymentMethod.objects.all()

            payment_method_list = []

            for payment in fatch_category:
                payment_method_data = {
                    'id': payment.id,
                    'payment_name': payment.payment_method,
                }
                payment_method_list.append(payment_method_data)
            # Render the template with the transaction data
            return render(request, 'payment.html', {
                'payments': payment_method_list,
            })
        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'payment method not found'}, status=400)


    def post(self, request):
            """Handle adding a new category (form POST)"""
            if request.content_type == 'application/json':
                try:
                    data = json.loads(request.body.decode('utf-8'))
                except json.JSONDecodeError:
                    return JsonResponse({'error': 'Invalid JSON'}, status=400)
            else:
                data = request.POST

            payment_name = data.get('name')
            if not payment_name:
                return JsonResponse({'error': 'Category name required'}, status=400)

            payment = PaymentMethod.objects.create(payment_method=payment_name)
            # print(payment)
            payment.save()
            return redirect('payment_show')


@method_decorator(csrf_exempt,name='dispatch')
class DeletePayment(View):
    def post(self,request,payment_id):
        try:
            fatch_payment = PaymentMethod.objects.get(id=payment_id)
            fatch_payment.delete()
            return redirect('payment_show')
            # return JsonResponse({'message': 'category delete successfully.'})
        
        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=400)    


@method_decorator(csrf_exempt,name='dispatch')
class UpdatePayment(View):
    # Show the edit form with current category
    def get(self, request, payment_id):
        try:
            payment = PaymentMethod.objects.get(id=payment_id)
            return render(request, 'payment_edit.html', {"payment": payment})
        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'Payment not found'}, status=404)
        
        

    # Handle form submission (update)
    def post(self,request, payment_id):
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        else:
            data = request.POST
        # category_id = data.get('id')

        payment_name = data.get('change_name')
        
        if not payment_name:
            return JsonResponse({'error': 'categroy name required'}, status= 400)
        
        try:
            fatch_payment = PaymentMethod.objects.get(id=payment_id)
            fatch_payment.payment_method = payment_name
            fatch_payment.save()

            # return JsonResponse({'message': 'category updated successfully.'})
            return redirect('payment_show')
        
        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=404)