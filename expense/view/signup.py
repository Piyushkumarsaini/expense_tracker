from django.shortcuts import render, redirect
from django.http import JsonResponse
from expense.models import *
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import re


# @method_decorator(csrf_exempt,name='dispatch')
class Signup(View):
    def get(self, request):
         return render(request, 'signup.html')
    


    def post(self,request):

        #------------------------------------------------ pass data for json----------------------------------------------
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        else:
            data = request.POST
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')


        # ------------------------------------------ Username Validatios ---------------------------------------------------------------------
        # username connot be empty
        if not username:
            return JsonResponse({'error': 'Username is Required'}, status= 400)
        
        # Remove all spaces
        elif username:
            username = username.replace(" ", "")
        
        # username length (4 to 20 characters)
        elif len(username) < 4:
            return JsonResponse({'error':'Username must be at least 4 characters long!'}, status=400)
        elif len(username) > 20:
            return JsonResponse({'error':'Username cannot be more than 20 characters!'}, status=400)
        
        # username must be alphanumeric(letters, number, underscore)
        elif not re.match(r'^[a-zA-Z0-9_]+$',username):
            return JsonResponse({'error':'Username can only contain letters, number and underscore!'}, status=400)
        
        # username must be unique
        # elif User.objects.filter(username=user_name).exists():
        #     return JsonResponse({'error': 'This username is already exists'}, status=400)


        # ---------------------------------------- Email Validatios ------------------------------------------------------
        # email connot be empty
        if not email:
            return JsonResponse({'error': 'Email is Required'}, status= 400)
        
        # Remove all spaces
        elif email:
            email = email.replace(" ", "")
        
        #  Validate email format using a simple regex
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            return JsonResponse({"error": "Invalid email format."}, status=400)
        
        # restrict email domains:
        if not email.endswith('@gmail.com'):
            return JsonResponse({'error': 'Only gmail address'}, status=400)
        
        # email must be unique
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'This email is already exists'}, status=400)
        
        # email length (max 254)
        elif len(email) > 254:
            return JsonResponse({'error':'Email id too long!'}, status=400)


        # ------------------------------------- Pssword Validatios -----------------------------------------------------
        # password connot be empty
        if not password:
            return JsonResponse({'error': 'Password is Required'}, status= 400)
        
        # password minimum length (8 characters)
        elif len(password) < 8:
            return JsonResponse({'error':'Password must be at least 8 characters long!'}, status=400)

        # password maximum length (128 characters)
        elif len(password) > 128:
            return JsonResponse({'error':'Password cannot be more than 128 characters!'}, status=400)
        
        # passwor must contain at least one uppercase letter
        elif not re.search(r'[A-Z]',password):
            return JsonResponse({'error':'Password must contain at least one uppercase letter!'}, status=400)

        # passwor must contain at least one lowercase letter
        elif not re.search(r'[a-z]',password):
            return JsonResponse({'error':'Password must contain at least one lowercase letter!'}, status=400)

        # passwor must contain at least one number
        elif not re.search(r'\d',password):
            return JsonResponse({'error':'Password must contain at least one number!'}, status=400)

        # passwor must contain at least one specilal character
        # elif not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        #     return JsonResponse({'error':'Password must contain at least one specilal character!'}, status=400)

        # # passwor must contain at least one specilal character
        # elif not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        #     return JsonResponse({'error':'Password must contain at least one specilal character!'}, status=400)

        # Password cannot be same as username
        elif password.lower() == username.lower():
            return JsonResponse({'error':'This password cannot be the same as  username!'}, status=400)


        # Password cannot be common (basic check)
        common_passwords = ['password', '12345678', 'qwertyui']
        if password.lower in common_passwords:
            return JsonResponse({'error':'This password is too common. Choose a stronger one!'}, status=400)



        # ---------------------------- Confirm Pssword Validatios --------------------------
        # confirm password connot be empty
        if not confirm_password:
            return JsonResponse({'error': 'Please confirm your password!'}, status= 400)
        
        # password and confirm password must match
        elif password != confirm_password:
            return JsonResponse({'error':'Passwords do not match!'}, status=400)
        

        #------------ password hashers -----------
        hashers_password = make_password(password)


        # -----------------------------------hold values ----------------------------
        # value = {
        #     'username': user_name,
        #     'email': email,
        #     'phone_number': phonenumber
        # }
        
        #----------------------------- save data for database -----------------------
        try:
            # create new user 
            user_save = User.objects.create(
                username =username,
                email=email,
                password=hashers_password
                )
            user_save.save()

            # Step 2: Assign first 6 default payment methods to this user
            default_methods = PaymentMethod.objects.all()[:6]
            user_payment_objects = []

            for method in default_methods:
                user_payment_objects.append(
                    UserPaymentMethod(user_id=user_save, payment_method=method)
                )

            UserPaymentMethod.objects.bulk_create(user_payment_objects) # bulk_create() → sabhi entries ko ek hi baar mein save kar diya (zyada fast & efficient).

            return JsonResponse({'message':'User Signup Successfully'},status=201)
        except Exception as e:
            return JsonResponse({'error':f'Something went wrong: {str(e)}'})

        
    