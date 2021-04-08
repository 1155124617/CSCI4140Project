from django.shortcuts import render
from .models import Client
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the bbs index.")

def clientProfile(request, client_id):
    client = Client.objects.get(id=client_id)
    return HttpResponse(f"This is {client.name}")
