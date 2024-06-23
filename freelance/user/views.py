from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail

from .helpers import email_generator

import re
from .models import User

# forget pass hashing
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def sign_up(request):
    return render(request, 'dashboard/registration.html')

def email_verify(request,id):

    vcode = id
    user = User.objects.get(v_code=vcode)
    user.v_status = 1 #Update User set v_status=1 Where v_code=v_code
    user.save()
    user_data = {"u_data":user}
    return render(request,'dashboard/congrats.html',user_data)

def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name,domain = email.split('@')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$"

        if( len(email) == 0 or len(password) == 0 or len(conf_password) == 0):
            messages.error(request, 'Empty field not accepted')
            print('iam')
        else:
            if(len(password)<3):
                messages.error(request,'The field length must be minimum 3')

            elif (password!=conf_password):
                messages.error(request, 'The password and confirm password does not match')

            elif not re.match(pattern, email):
                messages.error(request, 'Email is not validated')
            
            elif User.objects.filter(email=email).exists():
            # If a user with this email already exists, return an error message
                messages.error(request, 'Email is already exists!')
            else:
                # Encrypt the user pass
                Encrypt_password = make_password(password)

                v_code, link = email_generator(name)
                User.objects.create(email=email, password=Encrypt_password, v_code=v_code, v_status=0)
                
                send_mail(name ,link,'aminulmahi12@gmail.com',[email],html_message=link)
                messages.success(request, 'User Role created succesfully!')
                
                return HttpResponse('registration done')
                # return redirect('info_up')
            
    return render(request, 'dashboard/registration.html')
    