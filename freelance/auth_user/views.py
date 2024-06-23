from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User

from django.core.mail import send_mail
from .helpers import fp_email_generate

from django.core.exceptions import MultipleObjectsReturned

from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password

import base64
import re
# Create your views here.


def login(request):
    if 'user_id' in request.session:
        return redirect('user_home')
    else:
        return render(request, 'dashboard/login.html')
    
def logout(request):
    if 'user_id' in request.session:
        request.session.flush()
    return redirect('user_index')


def login_done(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pw = request.POST.get('password')  

        if(email == None and pw == None):
            messages.error(request, 'Empty field not accepted')

        else: 

            try:

                
                check = User.objects.get(email=email)
                                        # and check.v_status == '1'
                encrypt_pass = check.password
                print(encrypt_pass)
                if (check_password(pw, encrypt_pass)):
                    request.session['user_id'] = check.id     # set the variable name as userId 
                    print(request.session['user_id'])

                    return redirect('user_home')
                
            except User.DoesNotExist:
                messages.error(request, 'User does not exist!')

            except MultipleObjectsReturned:
                messages.error(request, 'This email is already registered!')

            return redirect('login')



######## forget password #########


# This fucntion for forgot password
def fp_emailindex(request):
    return render(request, 'dashboard/fp-emailindex.html')

# this function will send the email to the user when user press submit button at the beginning.
def fp_email_input(request):
    fp_email = request.POST.get('fp_email')
    name,domain = fp_email.split('@')
    user = User.objects.get(email=fp_email)

    user_id = user.id
    exist_password = user.password
    
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    if User.objects.filter(email=fp_email).exists():
        
        if len(fp_email) == 0:
            return HttpResponse("Empty Field not accepted")
        
        elif len(fp_email)<4:
                return HttpResponse("Minimum length of email and password is 4")
        elif not re.match(pattern, fp_email):
            return HttpResponse("Invalid email")
        
        else:
            vcode, link = fp_email_generate(name)
            user_obj = User(id = user_id, email= fp_email, password = exist_password, v_code=vcode, v_status = 0)
            user_obj.save()


            send_mail(name ,link,'aminulmahi12@gmail.com',[fp_email],html_message=link)
            messages.success(request, 'Your Password submitted successfully!')
            return redirect('fp_emailindex')
    else:
        return render(request, 'dashboard/fp_warning.html')
    

# after clicking the link in email this function will be called to take new password prompts.
def reset_password(request,id):
    print(id)
    all_user_data = User.objects.filter(v_code = id) # id is v_code
    if all_user_data.exists():
        user = all_user_data.first()
        print(user.email)
        print(user.id)
    user_data ={'user_data':all_user_data}
    return render(request, 'dashboard/fp_passwordinput.html',user_data)

#this function will be called during pressing on the email link. Which will reset the password finally.
def fp_email_verify(request,id): 
    user = User.objects.get(id=id)
    npassword = request.POST.get('newPassword')
    connpas = request.POST.get('confirmPassword')
    if npassword != connpas:
        return HttpResponse("Password does not matched")
    else:
        id = user.id
        password = make_password(npassword)
        email = user.email
        v_code = user.v_code
        v_status = 1
        
        reset_obj = User(id=id,  password=password, email=email, v_code=v_code, v_status=v_status)
        reset_obj.save()
        messages.success(request, 'Your Password changed successfully! please login')
        return redirect('login')