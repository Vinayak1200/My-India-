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
    # ['Booking ID:', param_dict['booking_id']],
    ['Name:', param_dict['name']],
    ['Booking date:', param_dict['date']],
    # ['Booking slot:', param_dict['booking_slot']],
    ['Adults :',param_dict['number_adults']],
    ['Children :',param_dict['number_children']],
    ['Booking amount :',param_dict['amount']],
    ['Parking amount :',param_dict['parking_amt']]
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