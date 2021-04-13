from django.shortcuts import render
from .models import Client
from .models import Book
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
import requests


def index(request):
    return HttpResponse("Hello, world. You're at the bbs index.")


def client_sign_in(request):
    context = {}
    if request.COOKIES.get('userid'):
        response = redirect("/bbs/client/main_page")
        return response
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

def client_main_page(request):
    context={}
    if request.method != "POST" and not request.COOKIES.get('userid'):
        return HttpResponse(status=404)
    elif not request.COOKIES.get('userid'):
        context['userid'] = 'UserID : ' + request.POST.get('id')
        template = loader.get_template('bbs/client/mainpage.html')
        res = HttpResponse(template.render(context,request))
        res.set_cookie('userid',request.POST.get('id'))
        return res
    else:
        context['userid'] = 'UserID : ' + request.COOKIES.get('userid')
        template = loader.get_template('bbs/client/mainpage.html')
        return HttpResponse(template.render(context,request))

def client_sign_out(request):
    context={}
    response = redirect('../signin')
    response.delete_cookie('userid')
    return response

def user_borrow_return(request):
    context = {}
    context['userid'] = 'UserID : ' + request.COOKIES.get('userid')
    template = loader.get_template('bbs/client/UserBorrow&Return.html')
    return HttpResponse(template.render(context,request))

def book_information_retrieval(request):
    context = {}
    context['userid'] = 'UserID : ' + request.COOKIES.get('userid')
    template = loader.get_template('bbs/client/BookInformationRetrieval.html')
    return HttpResponse(template.render(context,request))
    
def look_up_books(request):
    context = {}
    if request.method != 'POST':
        return HttpResponse(status=404)
    else:
        try:
            book = Book.objects.get(name=request.POST['book_name'])
            context['message'] = 'Successfully find the book named ' + request.POST['book_name']
            context['bookname'] = book.name
            context['bookid'] = book.id
            context['bookdesc'] = book.description
            context['bookloc'] = book.location
            context['bookborrowerid'] = book.borrower_id
            context['is_public'] = book.is_public
            print(book)
            template = loader.get_template('bbs/client/RetrievalResult.html')
            return HttpResponse(template.render(context,request))

        except ObjectDoesNotExist:
            print('ERROR')
            template = loader.get_template('bbs/client/BookInformationRetrieval.html')
            context['message'] = "No book named " + request.POST['book_name'] 
            return HttpResponse(template.render(context,request))


    
