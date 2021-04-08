from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('client/<int:client_id>/', views.clientProfile, name='clientProfile'),
    path('client/signin/', views.clientSignIn, name='clientSignIn'),
    path('client/signup/', views.clientSignUp, name='clientSignUp'),
]