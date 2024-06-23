from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("user_login/", views.login_done,name='login_done'),
    path('logout/', views.logout, name='logout'),
    path('fp_emailindex/', views.fp_emailindex, name='fp_emailindex'),
    path('fp_email_input/', views.fp_email_input, name='fp_email_input'),
    path("fp_email_verification/<str:id>", views.fp_email_verify,name='fp_email_verify'),
    path("reset_password/<str:id>", views.reset_password,name='reset_password'),
]