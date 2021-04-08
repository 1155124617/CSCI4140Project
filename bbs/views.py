from django.shortcuts import render
from .models import Client
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return HttpResponse("Hello, world. You're at the bbs index.")


def client_sign_in(request):
    context = {}
    if request.method == 'POST':
        try:
            Client.objects.get(email=request.POST['email'])
            print('ERROR')
            context["message"] = "The Email is used. Please select another email."
        except ObjectDoesNotExist:
            context["message"] = f"{request.POST['email']} is successfully registered."
            new_client = Client(
                email=request.POST['email'],
                password=request.POST['password'],
                phone_number=request.POST['phone'],
                name=request.POST['name'],
                major=request.POST['major'],
                grade=request.POST['grade']
            )
            new_client.save()

    return render(request, 'bbs/client/signin.html', context)


def client_sign_up(request):
    context = {}
    template = loader.get_template('bbs/client/signup.html')
    return HttpResponse(template.render(context, request))


def client_profile(request, client_id):
    client = Client.objects.get(id=client_id)
    return HttpResponse(f"This is {client.name}")