from django.shortcuts import render, redirect
from django.http import JsonResponse
from user.models import User
from django.contrib.auth.hashers import check_password
import json
import re
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



# @method_decorator(csrf_exempt,name='dispatch')
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self,request):

        #------------------------------------------------ pass data for json----------------------------------------------
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid Json Data'}, status=400)
        else:
            data = request.POST

        
        email = data.get('email')
        password = data.get('password')


        # ---------------------------------------- Email Validatios ------------------------------------------------------

        # Check if email is missing
        if not email:
            return JsonResponse({"error": "Email is required."}, status=400)
        
        # Remove spaces from email
        elif email:
            email = email.replace(" ", "")

        #  Validate email format using a simple regex
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

        try: 
            if user:
                hashers_password_to_text = check_password(password, user.password)
                if hashers_password_to_text:
                    request.session['user_id']= user.id
                    return JsonResponse({'message':'Login Successfully'}, status=200)
                else:
                    return JsonResponse({'error':'Email or Password Invalid.'})
            else:
                return JsonResponse({'error':'Email or Password Invalid.'})

        except Exception as e:
            # Handle any unexpected errors
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
