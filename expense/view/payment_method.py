from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



@method_decorator(csrf_exempt,name='dispatch')
class ShowPaymentMethod(View):
    def get(self,request):
        try:
            fatch_category = PaymentMethod.objects.all()

            payment_method_list = []

            for payment in fatch_category:
                payment_method_data = {
                    'id': payment.id,
                    'category_name': payment.payment_method,
                }
                payment_method_list.append(payment_method_data)
            return JsonResponse({'category_detale': payment_method_list}, safe=False)
        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'payment method not found'}, status=400)


@method_decorator(csrf_exempt,name='dispatch')
class PaymentMethodDetileAdd(View):
    def post(seld,request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'invalid json data'}, status=400)

        payment_method_name = data.get('name')
        if not payment_method_name:
            return JsonResponse({'error': 'categroy name required'}, status= 400)
        
        save_payment_method_datiles = PaymentMethod.objects.create(
            payment_method=payment_method_name
            )
        save_payment_method_datiles.save()
        return JsonResponse({'message':'categroy added succssfully'}, status=201)

    
        

@method_decorator(csrf_exempt,name='dispatch')
class DeletePaymentMethod(View):
    def delete(self,request,payment_method_id):
        try:
            fatch_payment_method = PaymentMethod.objects.get(id=payment_method_id)
            fatch_payment_method.delete()

            return JsonResponse({'message': 'category delete successfully.'})
        
        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=400)    


@method_decorator(csrf_exempt,name='dispatch')
class UpdatePaymentMethod(View):
    def patch(self, request, payment_method_id):

        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'invalid json data'}, status=400)
        
        try:
            fatch_payment_method = PaymentMethod.objects.get(id=payment_method_id)

            fatch_payment_method.payment_method = data.get('name',fatch_payment_method.payment_method)

            fatch_payment_method.save()

            return JsonResponse({'message':'category update succssfully'}, status=201)

        except PaymentMethod.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=400) 