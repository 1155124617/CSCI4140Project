from django.shortcuts import render
from .models import Client
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the bbs index.")

def clientProfile(request, client_id):
    client = Client.objects.get(id=client_id)
    return HttpResponse(f"This is {client.name}")

def clientSignIn(request):
    context = {}
    template = loader.get_template('bbs/client/signin.html')
    return HttpResponse(template.render(context, request))

def clientSignUp(request):
    context = {}
    template = loader.get_template('bbs/client/signup.html')
    return HttpResponse(template.render(context, request))

