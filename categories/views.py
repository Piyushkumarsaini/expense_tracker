from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from categories.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.exceptions import ObjectDoesNotExist



@method_decorator(csrf_exempt,name='dispatch')
class CategoriesShow(View):
    def get (self, request):
        user_id = request.session.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return render(request, 'login.html')
        
        try:
            fatch_categories = Category.objects.all()

            categories_list = []
            for categories in fatch_categories:
                categories_data = {
                    'id': categories.id,
                    'categories_name': categories.categories,
                }
                categories_list.append(categories_data)
            # Render the template with the transaction data
            return render(request, 'categories_show.html', {
                'categories': categories_list,
            })
            
        except Category.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=400)

    def post(self, request):
    
        user_id = request.session.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return render(request, 'login.html')
        
        
        """Handle adding a new category (form POST)"""
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        else:
            data = request.POST

        category_name = data.get('name')
        if not category_name:
            return JsonResponse({'error': 'Category name required'}, status=400)

        new_category = Category.objects.create(user=user,categories=category_name)
        new_category.save()
        return redirect('category_show')
    

@method_decorator(csrf_exempt, name='dispatch')
class CategoriesEdit(View):
    # Show the edit form with current category
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            return render(request, 'categories_edit.html', {"category": category})
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)

    # Handle form submission (update)
    def post(self,request, category_id):
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        else:
            data = request.POST
        # category_id = data.get('id')

        category_name = data.get('change_name')
        print(category_name)
        
        if not category_name:
            return JsonResponse({'error': 'categroy name required'}, status= 400)
        
        try:
            fatch_category = Category.objects.get(id=category_id)
            fatch_category.categories = category_name
            fatch_category.save()

            # return JsonResponse({'message': 'category updated successfully.'})
            return redirect('category_show')
        
        except Category.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=404)

        
@method_decorator(csrf_exempt,name='dispatch')
class CategoriesDelete(View):
    def post(self, request, category_id):
        try:
            fatch_category = Category.objects.get(id=category_id)
            fatch_category.delete()
            return redirect('category_show')
        except Category.DoesNotExist:
            return JsonResponse({'error': 'category not found'}, status=404)
        
        