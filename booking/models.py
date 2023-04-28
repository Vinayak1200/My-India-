from django.db import models
from PortalSem4 import settings
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, PermissionsMixin

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
INDIAN=0
NRI=1
NATIONALITY_CHOICES = [(INDIAN,'Indian'),(NRI,'NRI')]
NONE=0
CAR=1
BIKE=2
PARKING_CHOICES = [(NONE,'None'),(CAR,'Car'),(BIKE,'Bike')]

# Create your models here.
class Booking(models.Model):
    username = models.CharField(max_length=100,null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    numberchildren = models.IntegerField(null=True)
    nationality = models.IntegerField(choices=NATIONALITY_CHOICES)
    dateofvisit = models.DateField()
    age = models.CharField(max_length=3)
    numberadult = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    parking = models.IntegerField(choices=PARKING_CHOICES)
    
    
    
    
class CustomUser(AbstractUser):
    username=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True)
    # password = models.CharField(max_length=20,unique=True)
    phonenumber = models.CharField(max_length=12,unique=True)
    aadhaar = models.CharField(max_length=16,unique=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    

class Place(models.Model):
    PlaceId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, null=True)
    Location = models.CharField(max_length=200,null=True)
    
class Seats(models.Model):
    PlaceID = models.ForeignKey(Place, on_delete=models.CASCADE, unique=True)
    # SeatID = models.AutoField(primary_key=True)
    Vacancy = models.IntegerField(null=True)
    
    