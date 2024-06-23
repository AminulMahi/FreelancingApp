from django.shortcuts import render, redirect
from .models import User_info

from user.models import User

# Create your views here.

def user_profile(request):
    if 'user_id' in request.session:
        

        userid = request.session.get('user_id')

        user_all_data = User.objects.filter(id=userid).values('id', 'email')
        user_info_data = User_info.objects.filter(user_id=userid).values('name','title','address','description','rate','services')
        
        
        data = {'user_data': user_all_data, 'info_data': user_info_data}

        return render(request, 'dashboard/user-profile.html', data)
    return redirect('user_index')

    

def user_profile_settings(request):
    return render(request, 'dashboard/user-profile-settings.html')

def user_info_insert(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        title = request.POST.get('Title')
        address = request.POST.get('Address')
        description = request.POST.get('Description')
        rate = request.POST.get('Rate')
        services = request.POST.get('Services')

        userid = request.session.get('user_id')

        User_info.objects.create(name=name,title=title,address=address,description=description,rate=rate, services=services,user_id=userid)

        return redirect('user_profile')
    
    return redirect('user_profile_settings')