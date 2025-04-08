from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt,name='dispatch')
class Signup(View):
    def post(self,request):
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirmpassword')


        # user name validatio
        if not username:
            return JsonResponse({'error': 'User Name Required'}, status= 400)
        elif len(username) < 4:
            return JsonResponse({'error':'User Name must be 4 char long or more.'}, status=400)
        # elif User.objects.filter(username=user_name).exists():
        #     return JsonResponse({'error': 'User Name Already Exists'}, status=400)


        # email validatio
        if not email:
            return JsonResponse({'error': 'Email Required'}, status= 400)
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email Already Exists'}, status=400)


        # password validatio
        if not password:
            return JsonResponse({'error': 'Password Required'}, status= 400)
        # elif password > 8:
        #     return JsonResponse({'error':'Password must be 8 char long or more.'}, status=400)


        # confirm password validatio
        if not confirm_password:
            return JsonResponse({'error': 'Confirm Password Required'}, status= 400)
        elif confirm_password != password:
            return JsonResponse({'error':'Confirm Password Does Not Match The Password.'}, status=400)
            

        # password hashers
        hashers_password = make_password(password)


        # hold values 
        # value = {
        #     'username': user_name,
        #     'email': email,
        #     'phone_number': phonenumber
        # }
        
        # save data for databse
        user_save = User.objects.create(
            username =username,
            email=email,
            password=hashers_password        )

        user_save.save()

        return JsonResponse({'message':'User Signup Successfully'},status=201)
    