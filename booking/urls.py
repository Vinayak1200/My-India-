from django.urls import path, include 
from . import views

urlpatterns=[
     path('', views.index, name='index'),
     path('login', views.login, name='login'),
     path('signup', views.signup, name='signup'),
     path('contact',views.contact, name='contact'),
     path('destination',views.destination, name='destination'),
     path('NewDelhi', views.NewDelhi, name='NewDelhi'),
     path('TajMahal',views.TajMahal,name='TajMahal'),
     path('AgraFort',views.AgraFort,name='AgraFort'),
     path('IndiaGate',views.IndiaGate,name='IndiaGate'),
     path('Booking',views.Booking,name='Booking'),
     path('Booking-2', views.Booking2, name='Booking-2'),
     path('Booking-3',views.Booking3, name='Booking-3'),
     path('Downloadpdf',views.Downloadpdf,name='Downloadpdf'),
     path('AfterBooking', views.AfterBooking, name='AfterBooking'),
     path('handlerequest', views.handlerequest, name='handlerequest'),
     path('Akshardham', views.Akshardham,name='Akshardham'),
     path('paytm', views.paytm, name='paytm')
]
