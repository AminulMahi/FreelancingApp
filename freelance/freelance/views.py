from django.shortcuts import render, redirect

# from user.models import User

def user_index(request):
   
    return render(request, 'dashboard/index.html')



def user_home(request):
    if 'user_id' in request.session:

        userid = request.session.get('user_id')
        print(userid)

        # user_all_data = User.objects.filter(id=userid).values('name', 'id', 'email', 'phone', 'user_type')
        # user_info_data = Userinfo.objects.filter(user_id=userid).values('full_name', 'address', 'image')
        # print(user_info_data)
        
        
        # data = {'user_data': user_all_data, 'info_data': user_info_data}

        return render(request, 'dashboard/user_home.html')
    return redirect('user_index')



def user_profile(request):
    return render(request, 'dashboard/user-profile.html')