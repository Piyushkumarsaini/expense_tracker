from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
from django.contrib.auth.hashers import check_password, make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



@method_decorator(csrf_exempt,name='dispatch')
class ChangePassword(View):
    def post(self,request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        

        email = data.get('email')
        old_password = data.get('old_password')
        new_password = data.get('new_password')

        if not email:
            return JsonResponse({'error': 'Email Required'}, status= 400)
        
        elif not old_password:
            return JsonResponse({'error': 'Old Password Required'}, status= 400)
        
        elif not new_password:
            return JsonResponse({'error': 'Password Required'}, status= 400)
        
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'error':'This Email Does Not Exist.'})
        
             

        if check_password(old_password,user.password):
                user.password = make_password(new_password)
                user.save()
                return JsonResponse({'message':'Change Password Succssfully'}, status=201)
        else:
            return JsonResponse({'error': 'Old Password Incorrect'}, status=400)

        