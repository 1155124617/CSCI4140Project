from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('client/<int:client_id>/', views.client_profile, name='clientProfile'),
    path('client/signin/', views.client_sign_in, name='clientSignIn'),
    path('client/signup/', views.client_sign_up, name='clientSignUp'),
    path('client/main_page/', views.client_main_page, name='clientMainPage'),
    path('client/signout/',views.client_sign_out,name='ClientSignOut'),
    path('client/UserBorrow&Return/',views.user_borrow_return,name='UserBorrow&Return'),
    path('client/BookInformationRetrieval/',views.book_information_retrieval,name='BookInformationRetrieval'),
    path('client/lookupbooks/',views.look_up_books,name='lookupbooks'),
    path('client/borrow&return/',views.borrow_return,name='borrow&return'),
    path('client/booktransfer/',views.book_transfer,name="booktransfer"),
    path('client/booktransferaccept/',views.book_transfer_accept,name="booktransferaccept"),
    path('client/booktransferrequest/',views.book_transfer_request,name="booktransferrequest"),
    path('client/booktransferconfirmation/',views.book_transfer_confirmation,name="booktransferconfirmation")
]