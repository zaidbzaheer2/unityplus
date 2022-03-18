from . import views
from django.urls import path, include

urlpatterns = [
    path('register/',views.signUpPage, name='RegisterPage'),
    path('login/', views.loginPage, name='LoginPage') 
]