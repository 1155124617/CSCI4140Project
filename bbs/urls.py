from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('client/<int:client_id>/', views.clientProfile, name='clientProfile'),
]