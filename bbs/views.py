from django.shortcuts import render
from .models import Client
from .models import Book
from .models import TransferRequest
from .models import Reservation
from .models import Transfer
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
import requests
import time
import datetime
import sqlite3

import socket

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
        try:
            client = Client.objects.get(id=request.POST['id'],password=request.POST['pass'])
            template = loader.get_template('bbs/client/mainpage.html')
            res = HttpResponse(template.render(context,request))
            res.set_cookie('userid',request.POST.get('id'))
            return res
        except:
            print('wrong pass')
            res = redirect('../signin/')
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
    books = Book.objects.filter(borrower_id=request.COOKIES.get('userid'))
    context['books'] = books
    if len(books) != 0:
        context['message'] = "Below are book(s) that you have borrowed"
    else:
        context['message'] = "You haven't borrowed any book"
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
        context['userid'] = 'UserID : ' + request.COOKIES.get('userid')
        try:
            if request.POST['book_id']:
                books = Book.objects.filter(id=request.POST['book_id'])
                if len(books) == 0:
                    template = loader.get_template('bbs/client/BookInformationRetrieval.html')
                    context['message'] = "No satisfied book, please try other words"
                    return HttpResponse(template.render(context,request))
                else:
                    context['message'] = 'Successfully find the book with id ' + request.POST['book_id']
                    context['books'] = books

                    template = loader.get_template('bbs/client/RetrievalResult.html')
                    return HttpResponse(template.render(context,request))

            elif request.POST['book_location'] != 'N/A':
                books = Book.objects.filter(name=request.POST['book_name'],location=request.POST['book_location'])
                if len(books) == 0:
                    template = loader.get_template('bbs/client/BookInformationRetrieval.html')
                    context['message'] = "No satisfied book, please try other words"
                    return HttpResponse(template.render(context,request))
                else:
                    context['message'] = 'Successfully find the book with name ' + request.POST['book_name'] + " and location " + request.POST['book_location']
                    context['books'] = books

                    template = loader.get_template('bbs/client/RetrievalResult.html')
                    return HttpResponse(template.render(context,request))

            else:
                books = Book.objects.filter(name=request.POST['book_name'])
                if len(books) == 0:
                    template = loader.get_template('bbs/client/BookInformationRetrieval.html')
                    context['message'] = "No satisfied book, please try other words"
                    return HttpResponse(template.render(context,request))
                else:
                    context['message'] = 'Successfully find the book with name ' + request.POST['book_name']
                    context['books'] = books

                    context['valid'] = False
                    for book in books:
                        if book.borrower_id == 0:
                            context['valid'] = True
                            break
                    context['book_name'] = request.POST['book_name']

                    template = loader.get_template('bbs/client/RetrievalResult.html')
                    return HttpResponse(template.render(context,request))

        except ObjectDoesNotExist:
            print('ERROR')
            template = loader.get_template('bbs/client/BookInformationRetrieval.html')
            context['message'] = "No satisfied book, please try other words"
            return HttpResponse(template.render(context,request))


def borrow_return(request):
    context = {}
    if request.method != 'POST':
        return HttpResponse(status=404)
    else:
        if request.POST['form_method'] == 'Borrow':
            try:
                book = Book.objects.get(id=request.POST['book_id'],borrower_id=0)
                book.borrower_id = request.COOKIES.get('userid')
                book.save()
                context['message'] = 'You have successfully borrowed the book'
            except:
                context['message'] = 'The requested book has been borrowed by the other one'

        else:
            # try:
            book = Book.objects.get(id=request.POST['book_id'],borrower_id=request.COOKIES.get('userid'))
            book.borrower_id = 0
            book.save()

            reservations = Reservation.objects.filter(book_name=book.name, is_book_valid=False, is_finished=False)

            if len(reservations) > 0:
                time_now = datetime.datetime.now()
                time = (time_now + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

                reservation = reservations[0]
                reservation.is_book_valid = True
                reservation.book_id = book.id
                reservation.location = book.location
                reservation.valid_date = time
                reservation.save()

            context['message'] = 'You have successfully returned the book'
            # except:
            #     context['message'] = 'You currently do not have this book borrowed or you have returned it already'

    template = loader.get_template('bbs/client/Borrow&ReturnResult.html')
    return HttpResponse(template.render(context,request))


def book_transfer(request):
    context = {}
    context['userid'] = "User ID : " + request.COOKIES.get('userid')
    books = Book.objects.filter(borrower_id=request.COOKIES.get('userid'), is_public = True)
    
    req = set()
    flag = 0
    for book in books:
        result = TransferRequest.objects.filter(book_name=book.name)
        if len(result) != 0:
            if flag == 0:
                req = result
                flag += 1
            else:
                req.join(result)
    context['requests'] = req

    if len(req) != 0:
        context['message'] = "Below are book(s) that you have borrowed which are requested by others"
    else:
        context['message'] = "There are no requests related to the books that you borrowed"

    template = loader.get_template('bbs/client/BookTransfer.html')
    return HttpResponse(template.render(context,request))

def book_transfer_accept(request):
    context = {}
    context['userid'] = "User ID : " + request.COOKIES.get('userid')
    if request.method != 'POST':
        return HttpResponse(status=404)
    else:
        try:
            req = TransferRequest.objects.get(id=request.POST['request_id'])
            new_transfer = Transfer(
                transfer_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
                borrower_id = req.borrower_id,
                lender_id = request.COOKIES.get('userid'),
                book_id = Book.objects.filter(
                    name = req.book_name, 
                    borrower_id = request.COOKIES.get('userid'),
                    is_public=True
                )[:1].get().id,
                img = "NULL",
                borrower_confirm = False,
                lender_confirm = False
            )
            new_transfer.save()
            req.delete()
            context['message'] = "Accept Successfully!"
        except:
            context['message'] = "The request id doesn't exit!"
        
        template = loader.get_template("bbs/client/BookTransferAccept.html")
        return HttpResponse(template.render(context,request))


def book_transfer_request(request):
    context = {}
    context['userid'] = "User ID : " + request.COOKIES.get('userid')
    if request.method != 'POST':
        return HttpResponse(status=404)
    else:
        try:
            request_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            
            #request_location = get_geolocation_for_ip(get_client_ip(request))
            request_location = request.POST['Location']

            request_id = request.COOKIES.get('userid')

            bookname = request.POST['book_name']

            message = request.POST['message']

            new_request = TransferRequest(
                borrower_id=request_id,
                book_name=bookname,
                request_time=request_time,
                location=request_location,
                message=message
            )
            new_request.save()
            context['message'] = "Request Successfully!"
        except Exception as e:
            context['message'] = "The Request Failed!"
            print(e)

        template = loader.get_template("bbs/client/BookTransferAccept.html")
        return HttpResponse(template.render(context,request))


def book_transfer_confirmation(request):
    context = {}
    if request.method == "POST":
        try: 
            request.POST['lender_transfer_id']
            try:
                print(request.FILES['image'].read())
                transfer = Transfer.objects.get(id = request.POST['lender_transfer_id'], lender_id = request.COOKIES['userid']) 
                transfer.lender_confirm = True
                transfer.img = sqlite3.Binary(request.FILES['image'].read())
                transfer.save()
                if transfer.borrower_confirm == True:
                    book = Book.objects.get(id = transfer.book_id)
                    book.borrower_id = transfer.borrower_id
                    book.save()
                context['warning'] = "Successfully Confirm"
            except Exception as e:
                context['warning'] = e
                print(e)

        except:
            try:
                transfer = Transfer.objects.get(id = request.POST['borrower_transfer_id'], borrower_id = request.COOKIES['userid'])
                transfer.borrower_confirm = True
                transfer.save()
                if transfer.lender_confirm == True:
                    book = Book.objects.get(id = transfer.book_id)
                    book.borrower_id = transfer.borrower_id
                    book.save()
                context['warning'] = "Successfully Confirm"
            except:
                context['warning'] = "Confirmation failed"
    
    context['userid'] = "User ID : " + request.COOKIES.get('userid')
    transfers_lender = Transfer.objects.filter(lender_id = request.COOKIES.get('userid'),lender_confirm=False)
    transfers_lender |= Transfer.objects.filter(lender_id = request.COOKIES.get('userid'),borrower_confirm=False)
    transfers_borrower = Transfer.objects.filter(borrower_id = request.COOKIES.get('userid'),lender_confirm=False)
    transfers_borrower |= Transfer.objects.filter(borrower_id = request.COOKIES.get('userid'),borrower_confirm=False)
    if len(transfers_lender) == 0:
        context['message_lender'] = "No lending transfers"
    else:
        context['message_lender'] = "Below is your lending transfers"
    context['transfers_lender']  = transfers_lender

    if len(transfers_borrower) == 0:
        context['message_borrower'] = "No borrowing transfers"
    else:
        context['message_borrower'] = "Below is your borrowing transfers"
    context['transfers_borrower']  = transfers_borrower

    template = loader.get_template("bbs/client/BookTransferConfirmation.html")
    return HttpResponse(template.render(context,request))


def reservations(request):
    context = {}
    context['userid'] = 'UserID : ' + request.COOKIES.get('userid')
    d = datetime.date.today()
    reservations = Reservation.objects.filter(borrower_id=request.COOKIES.get('userid'), is_finished=False, valid_date__gte=d)

    context['reservations'] = reservations
    if len(reservations) == 0:
        context['message'] = "You don't have a valid reservation"
    else:
        context['message'] = "Below are reservation(s) that you have"

    template = loader.get_template('bbs/client/Reservations.html')
    return HttpResponse(template.render(context, request))

def reservations_borrow(request):
    context = {}
    if request.method != 'POST':
        return HttpResponse(status=404)
    else:
        try:
            reservation = Reservation.objects.get(id=int(request.POST['reservation_id']))
            reservation.is_finished = True
            reservation.save()
            book = Book.objects.get(id=reservation.book_id)
            book.borrower_id = request.COOKIES.get('userid')
            book.save()
            context['message'] = "Success!"
        except:
            context['message'] = 'Your reservation is failed. Please apply again.'


    context['userid'] = 'UserID : ' + request.COOKIES.get('userid')

    template = loader.get_template('bbs/client/Reservations.html')
    return HttpResponse(template.render(context, request))


def reservation_generate(request):
    context = {}
    if request.method != 'POST':
        return HttpResponse(status=404)
    else:
        try:
            reservation = Reservation(
                borrower_id=request.COOKIES.get('userid'),
                book_name=request.POST['book_name'],
                is_book_valid=False,
                is_finished=False
            )
            reservation.save()
            context['message'] = "Success!"
        except:
            context['message'] = 'Your reservation is failed. Please apply again.'

    context['userid'] = 'UserID : ' + request.COOKIES.get('userid')

    template = loader.get_template('bbs/client/Reservations.html')
    return HttpResponse(template.render(context, request))

