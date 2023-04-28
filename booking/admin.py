from django.contrib import admin
from .models import Booking, Place, Seats,CustomUser

# Register your models here.
admin.site.register([Booking, Place, Seats,CustomUser])