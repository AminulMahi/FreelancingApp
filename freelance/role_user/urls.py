from django.urls import path, include
from . import views

urlpatterns = [
    path('user_profile/',views.user_profile, name='user_profile'),
    path('user_profile_settings/',views.user_profile_settings, name='user_profile_settings'),
    path('user_info_insert/',views.user_info_insert, name='user_info_insert'),
]