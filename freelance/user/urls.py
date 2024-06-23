from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.sign_up, name='signup_page'),
    path('signup_form/', views.create_user, name='create_user'),
    
    path("email_verification/<str:id>", views.email_verify,name='email_verify'),
    
]
