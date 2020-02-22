from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main_index'),
    path('signup/', views.signup, name='main_signup'),
    path('signin/', views.signin, name='main_signin'),
    path('verifycode/', views.verifycode, name='main_verifycode'),
    path('verify/', views.verify, name='main_verify'),
    path('result/', views.result, name='main_result'),
]