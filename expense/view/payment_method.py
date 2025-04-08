from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



# @method_decorator(csrf_exempt,name='dispatch')
# class ShowPaymentMethod(View):
#     def get(self,request):
#         try:
#             fatch_category = PatmentMethod.objects.all()

#             patment_method_list = []

#             for patment in fatch_category:
#                 patment_method_data = {
#                     'id': patment.id,
#                     'category_name': patment.patment_method,
#                 }
#                 patment_method_list.append(patment_method_data)
#             return JsonResponse({'category_detale': patment_method_list}, safe=False)
#         except PatmentMethod.DoesNotExist:
#             return JsonResponse({'error': 'patment method not found'}, status=400)


@method_decorator(csrf_exempt,name='dispatch')
class PaymentMethodDetileAdd(View):
    def post(seld,request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'invalid json data'}, status=400)

        patment_method_name = data.get('name')
        if not patment_method_name:
            return JsonResponse({'error': 'categroy name required'}, status= 400)
        
        save_patment_method_datiles = PatmentMethod.objects.create(
            patment_method=patment_method_name
            )
        save_patment_method_datiles.save()
        return JsonResponse({'message':'categroy added succssfully'}, status=201)

    
        

# @method_decorator(csrf_exempt,name='dispatch')
# class DeletePaymentMethod(View):
#     def delete(self,request,patment_method_id):
#         try:
#             fatch_patment_method = PatmentMethod.objects.get(id=patment_method_id)
#             fatch_patment_method.delete()

#             return JsonResponse({'message': 'category delete successfully.'})
        
#         except PatmentMethod.DoesNotExist:
#             return JsonResponse({'error': 'category not found'}, status=400)    


# @method_decorator(csrf_exempt,name='dispatch')
# class UpdatePaymentMethod(View):
#     def patch(self, request, patment_method_id):

#         try:
#             data = json.loads(request.body.decode('utf-8'))
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'invalid json data'}, status=400)
        
#         try:
#             fatch_patment_method = PatmentMethod.objects.get(id=patment_method_id)

#             fatch_patment_method.patment_method = data.get('name',fatch_patment_method.patment_method)

#             fatch_patment_method.save()

#             return JsonResponse({'message':'category update succssfully'}, status=201)

#         except PatmentMethod.DoesNotExist:
#             return JsonResponse({'error': 'category not found'}, status=400) 