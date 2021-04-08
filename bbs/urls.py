from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('client/<int:client_id>/', views.client_profile, name='clientProfile'),
    path('client/signin/', views.client_sign_in, name='clientSignIn'),
    path('client/signup/', views.client_sign_up, name='clientSignUp'),
]