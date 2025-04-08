from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
from django.contrib.auth.hashers import check_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



@method_decorator(csrf_exempt,name='dispatch')
class Login(View):
    def post(self,request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'error':'This Email Does Not Exist.'})
        if user:
            hashers_password_to_text = check_password(password, user.password)
            if hashers_password_to_text:
                # request.session['user_id']= user.id
                # request.session['email']= user.email
                return JsonResponse({'message':'Login Successfully'})
            else:
                return JsonResponse({'error':'Email or Password Invalid.'})
        else:
            return JsonResponse({'error':'Email or Password Invalid.'})
