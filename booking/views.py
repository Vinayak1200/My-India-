from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import checksum
from .models import Booking,CustomUser
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import date

cluster = MongoClient("mongodb+srv://vinayak:2468@cluster0.ed2zc1e.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = cluster['BookingDB']
collection = db['booking']


MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

cluster = MongoClient("mongodb+srv://vinayak:2468@cluster0.ed2zc1e.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = cluster['BookingDB']
collection = db['booking']
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
import io
import pyqrcode

def GeneratePDF(param_dict):
    GeneratePDF.counter+=1
    imgname = 'img{f}'.format(f=GeneratePDF.counter)
    imgpath = imgname.join('.png')
    buffer = io.BytesIO()
    pagesize = (8 * inch, 7.5 * inch)
    
    # Generate QR code from booking details
    qr = pyqrcode.create(str(param_dict))
    qr_img_path = 'qr_code.png'
    qr.png(qr_img_path)
    
    details_data = [
    ['BOOKING DETAILS FOR', param_dict['name']],
    ['Name:', param_dict['name']],
    ['Booking date:', param_dict['date']],
    ['Adults :',param_dict['number_adults']],
    ['Children :',param_dict['number_children']],
    ['Booking amount :',param_dict['amount']],
    ['Parking amount :',param_dict['parking_amt']],
    ['Destination:', ''],
]
    
    doc = SimpleDocTemplate(buffer, pagesize=pagesize)

    # Define elements for the PDF
    elements = []
    # details_table = Table(details_data)
    details_table = Table(details_data,colWidths=[doc.width],rowHeights=[22 for i in range(8)])
    details_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightskyblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
    ('GRID', (0, 0), (-1, -1), 1, colors.whitesmoke)
]))
    elements.append(Image('MHI.png', height=60, width=60 ))
    elements.append(details_table)
    qr_code_img = Image(qr_img_path, width=120, height=120)
    elements.append(Spacer(0.5, 1))
    elements.append(qr_code_img)
    
    buffer.seek(0)
    
    return buffer
    
    
GeneratePDF.counter=0

def signup(request):
    return render(request, 'booking/signup.html')


def login(request):
    if request.method=='POST':
        
        print('Post successful\n')
        Username = request.POST.get('cust_name')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Aadhaar = request.POST.get('id_credential')
        PhoneNo = request.POST.get('cust_phone_number')
        
        
        user = CustomUser(username=Username, email=Email, password=Password,aadhaar=Aadhaar,phonenumber=PhoneNo)
        user.save()
    return render(request, 'booking/login.html')
    # else:return HttpResponse("Oops!Looks like something went wrong :(")

# Create your views here.

def index(request):
    if request.method=='POST':
        print(request)
        print('Post succesful again')
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = db.booking_customuser.find_one({'username':username, 'password':pwd})
        if user:
            print(user)
            return render(request, 'booking/index.html')
        else:
            messages.error('Login unsuccessful')
            return redirect('login')        
    return render(request, 'booking/index.html')

def contact(request):
    return render(request,'booking/contact.html')

def destination(request):
    return render(request,'booking/destination.html')

def NewDelhi(request):
    return render(request, 'booking/NewDelhi.html')

def Booking(request):
    return render(request, 'booking/Booking.html')

def Booking2(request):
    if request.method=='POST':
        print("POST successful")
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        numberA = request.POST.get('numberA')
        numberC = request.POST.get('numberC')
        country = request.POST.get('country')
        nationality = request.POST.get('nationality')
        parking = request.POST.get('parking')
        date = request.POST.get('dateofvisit')
        print(date)
        print(parking)
        base_amt = 100
        parking_amt = float()
        if parking=='Car':
            parking_amt=30
        else:parking_amt=15
        
        
        amount = int(numberA)*base_amt + int(numberC)*(0.5*base_amt)
        params = {'name':name,'gender':gender,'age':age,'number_adults':numberA,'number_children':numberC,'country':country,'nationality':nationality,'parking':parking,'date':date,'amount':amount,'parking_amt':parking_amt}
    return render(request, 'booking/Booking-2.html',context=params)

def Booking3(request):
    if request.method=='POST':
        print("POST successful")
        hiddenname = request.POST.get('hiddenname')
        hiddengender = request.POST.get('hiddengender')
        hiddenage = request.POST.get('hiddenage')
        hiddennumberA = request.POST.get('hiddennumberA')
        hiddennumberC = request.POST.get('hiddennumberC')
        hiddencountry = request.POST.get('hiddencountry')
        hiddennationality = request.POST.get('hiddennationality')
        hiddenparking = request.POST.get('hiddenparking')
        hiddendate = request.POST.get('hiddendateofvisit')
        ticket_price = request.POST.get('ticket_price')
        parking_price = request.POST.get('parking_price')
        params = {'name':hiddenname,'gender':hiddengender,'age':hiddenage,'number_adults':hiddennumberA,'number_children':hiddennumberC,'country':hiddencountry,'nationality':hiddennationality,'parking':hiddenparking,'date':hiddendate,'amount':ticket_price,'parking_amt':parking_price,'tot_amt':ticket_price+parking_price,'number_people':hiddennumberA+hiddennumberC}
        print(hiddendate)
        db.booking_booking.insert_one(params)
    return render(request, 'booking/Booking-3.html', context=params)

def Downloadpdf(request):
    name = request.GET.get('name')
    numberA = request.GET.get('number_adults')
    numberC = request.GET.get('number_children')
    date = request.GET.get('date')
    amount = request.GET.get('amount')
    parking_amt = request.GET.get('parking_amt')
    datadict = {
        'name':name,
        'number_adults':numberA,
        'number_children':numberC,
        'date':date,
        'amount':amount,
        'parking_amt':amount
    }
    
    buffer = GeneratePDF(datadict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=ticket.pdf'
    response.write(buffer.getvalue())
    buffer.close()

    return response

    


def AfterBooking(request):
    if request.method=='POST':
        print("POST successful")
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        numberA = request.POST.get('numberA')
        numberC = request.POST.get('numberC')
        country = request.POST.get('country')
        nationality = request.POST.get('nationality')
        parking = request.POST.get('parking')
        date = request.POST.get('dateofvisit')
        print(date)
        
        base_amt = 100
        car_amt=60
        bike_amt=40
        
        amount = int(numberA)*base_amt + int(numberC)*(0.5*base_amt)
        params = {'name':name,'gender':gender,'age':age,'number adults':numberA,'number children':numberC,'country':country,'nationality':nationality,'parking':parking,'date':date,'amount':amount,'parking_amt':car_amt}
        
        # bookingdata = [date, time, numberA, numberC, str(amount)]
        obj = db.booking_booking.insert_one(params)
        
       
        
        # obj = Booking(BookingDate = date, BookingSlot=time, NumberOfAdults=numberA, NumberOfChildren=numberC, Amount=amount)
        # obj.save()
        # buffer = GeneratePDF(bookingdata)
        # return FileResponse(buffer, as_attachment=True, filename='ticket.pdf')
        
        param_dict={
        "MID": "WorldP64425807474247",
        "ORDER_ID": obj.inserted_id,
        "TXN_AMOUNT": str(amount),
        "CUST_ID": 'acfff@paytm.com',
        "INDUSTRY_TYPE_ID": "Retail",
        "WEBSITE": "WEBSTAGING",
        "CHANNEL_ID": "WEB",
        'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',
        'CHECKSUMHASH':''
         }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'booking/paytm.html', context={'param_dict':param_dict})
        #  return render(request, 'booking/AfterBooking.html', context=dict(bookingdata))
    else:return HttpResponse("Sorry, there was some error in the backend")
    
def paytm(request):
    return render(request, 'booking/paytm.html')
    
@csrf_exempt    
def handlerequest(request):
     form = request.POST
     response_dict = {}
     for i in form.keys():
         response_dict[i] = form[i]
         if i == 'CHECKSUMHASH':
             checksum = form[i]
 
     verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
     if verify:
         if response_dict['RESPCODE'] == '01':
             print('booking successful')
         else:
             print('booking was not successful because' + response_dict['RESPMSG'])
     return render(request, 'booking/paymentstatus.html', {'response': response_dict})
        
# def paytm(request):
    # 
    