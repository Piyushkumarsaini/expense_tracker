from django.shortcuts import render, redirect
from expense.models import *
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
import json
import re
from django.db.models import Sum
from django.views import View
from django.contrib.auth.hashers import make_password



class VerifyEmail(View):
    def post(request):
     if request.method == 'GET':
          return render(request, 'verifyemail.html')
         
     if request.method == 'POST':
          if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
          else:
               data = request.POST
          email = data.get('email')


        # ---------------------------------------- Email Validatios ------------------------------------------------------

        # Check if email is missing
          if not email:
               return JsonResponse({"error": "Email is required."}, status=400)
        # Remove spaces from email
          elif email:
               email = email.replace(" ", "")

          email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
          if not re.match(email_regex, email):
               return JsonResponse({"error": "Invalid email format."}, status=400) 

          # email length (max 254)
          elif len(email) > 254:
               return JsonResponse({'error':'Email id too long!'}, status=400)
          
          # restrict email domains:
          if not email.endswith('@gmail.com'):
               return JsonResponse({'error': 'Invalid email format'}, status=400)

          try:
               user = User.objects.get(email=email)
          except:
               return JsonResponse({'error':'This Email Does Not Exist.'}, status=400)
          
          if user:
               request.session['user_email']= user.email
               return JsonResponse({'message':'Sand OTP'},status=201)
          
     return render(request, 'forgottpassword1.html')


def set_new_password(request):
     if request.method == 'GET':
          return render(request, 'setnewpassword.html')

     if request.method == 'POST':
          if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
          else:
            data = request.POST

          new_password = data.get('password')
          confirm_password = data.get('confirm_password')
          email = request.session.get('user_email')

          # ------------------------------------- Pssword Validatios -----------------------------------------------------
          # password connot be empty
          if not new_password:
               return JsonResponse({'error': 'Password is Required'}, status= 400)
          
          # password minimum length (8 characters)
          elif len(new_password) < 8:
               return JsonResponse({'error':'Password must be at least 8 characters long!'}, status=400)

          # password maximum length (128 characters)
          elif len(new_password) > 128:
               return JsonResponse({'error':'Password cannot be more than 128 characters!'}, status=400)
          
          # passwor must contain at least one uppercase letter
          elif not re.search(r'[A-Z]',new_password):
               return JsonResponse({'error':'Password must contain at least one uppercase letter!'}, status=400)

          # passwor must contain at least one lowercase letter
          elif not re.search(r'[a-z]',new_password):
               return JsonResponse({'error':'Password must contain at least one lowercase letter!'}, status=400)

          # passwor must contain at least one number
          elif not re.search(r'\d',new_password):
               return JsonResponse({'error':'Password must contain at least one number!'}, status=400)

          # passwor must contain at least one specilal character
          elif not re.search(r'[!@#$%^&*(),.?":{}|<>]',new_password):
               return JsonResponse({'error':'Password must contain at least one specilal character!'}, status=400)

          # passwor must contain at least one specilal character
          elif not re.search(r'[!@#$%^&*(),.?":{}|<>]',new_password):
               return JsonResponse({'error':'Password must contain at least one specilal character!'}, status=400)
          
          # Password cannot be common (basic check)
          common_passwords = ['password', '12345678', 'qwertyui']
          if new_password.lower in common_passwords:
               return JsonResponse({'error':'This password is too common. Choose a stronger one!'}, status=400)



          # ---------------------------- Confirm Pssword Validatios --------------------------
          # confirm password connot be empty
          if not confirm_password:
               return JsonResponse({'error': 'Please confirm your password!'}, status= 400)
          
          # password and confirm password must match
          elif new_password != confirm_password:
               return JsonResponse({'error':'Passwords do not match!'}, status=400)
          

          user = User.objects.get(email=email)
          hashers_password = make_password(new_password)


          #----------------------------- save data for database -----------------------
          try:
               # create new user 
               user.password = hashers_password
               user.save()
               return JsonResponse({'message':'Password reset successfully'},status=201)
          except Exception as e:
               return JsonResponse({'error':f'Something went wrong: {str(e)}'})
