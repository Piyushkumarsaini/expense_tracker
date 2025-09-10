# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from expense.models import *
# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views import View


# @method_decorator(csrf_exempt,name='dispatch')
# class Budget(View):
#     def post(self,request):
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'invalid json data'}, status=400)
        
#         user_id = data.get('id')
#         if not user_id:
#             return JsonResponse({'error': 'user id required'}, status= 400)
        

#         amount = data.get('amount')
#         if not amount:
#             return JsonResponse({'error': 'amount required'}, status= 400)
        
#         source = data.get('source')
#         if not source:
#             return JsonResponse({'error': 'source required'}, status= 400)
                
#         try:
#             fetch_user = User.objects.get(id=user_id)

#             save_income_datiles = income.objects.create(
#                 user_id=fetch_user,
#                 amount=amount,
#                 source=source
#                 )
            
#             save_income_datiles.save()
#             return JsonResponse({'message':'income added succssfully', 'income_id':income.id}, status=201)
        
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'user not found'}, status=400)