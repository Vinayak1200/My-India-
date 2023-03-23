from django.urls import re_path, include 
from . import views

urlpatterns=[
    re_path('', views.Book),
    re_path('thankyou', views.thankyou),
]