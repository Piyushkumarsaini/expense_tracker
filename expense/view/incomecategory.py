# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from expense.models import *
# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views import View



# @method_decorator(csrf_exempt,name='dispatch')
# class CategoryDetail(View):
#     def get(self,request):
#         try:
#             fatch_category = IncomeCategory.objects.all()

#             category_list = []

#             for category in fatch_category:
#                 category_data = {
#                     'id': category.id,
#                     'category_name': category.income_category,
#                 }
#                 category_list.append(category_data)
#             return JsonResponse({'category_detale': category_list}, safe=False)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'user not found'}, status=400)

#     def post(seld,request):
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'invalid json data'}, status=400)

#         category_name = data.get('name')
#         if not category_name:
#             return JsonResponse({'error': 'categroy name required'}, status= 400)
        
#         save_income_datiles = IncomeCategory.objects.create(
#             income_category=category_name
#             )
#         save_income_datiles.save()
#         return JsonResponse({'message':'categroy added succssfully'}, status=201)

    
        

#     def delete(self,request,category_id):
#         try:
#             fatch_income = IncomeCategory.objects.get(id=category_id)
#             fatch_income.delete()

#             return JsonResponse({'message': 'category delete successfully.'})
        
#         except IncomeCategory.DoesNotExist:
#             return JsonResponse({'error': 'category not found'}, status=400)    


#     def patch(self, request, category_id):

#         try:
#             data = json.loads(request.body.decode('utf-8'))
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'invalid json data'}, status=400)
        
#         try:
#             fetch_category = IncomeCategory.objects.get(id=category_id)

#             fetch_category.income_category = data.get('name',fetch_category.income_category)

#             fetch_category.save()

#             return JsonResponse({'message':'category update succssfully'}, status=201)

#         except IncomeCategory.DoesNotExist:
#             return JsonResponse({'error': 'category not found'}, status=400) 