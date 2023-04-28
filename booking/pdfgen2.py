from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Image, PageTemplate,Frame
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pyqrcode
from reportlab.lib.units import mm, inch
from qrcode.constants import ERROR_CORRECT_H

# Define your booking details here
booking_details = {
    'booking_id': '12345',
    'name': 'Vinayak Abrol',
    'booking_date': '2023-05-01',
    'Number of adults':'2',
    'Number of children':'1',
    'booking_slot': '11:00 AM',
    'place': 'Taj Mahal',
}
page_width, page_height = letter
spacer_height = page_height - 300
pagesize = (8 * inch, 7.5 * inch)  # 20 inch width and 10 inch height.

# Generate QR code from booking details
qr = pyqrcode.create(str(booking_details))
qr_img_path = 'qr_code.png'
qr.png(qr_img_path)

# Create a landscape-oriented PDF
doc = SimpleDocTemplate("ticket.pdf", pagesize=pagesize)

# Define elements for the PDF
elements = []

# def header(canvas, doc):
    # canvas.saveState()
    # canvas.drawImage("MHI.png", 0, doc.pagesize[0], width=75, height=75)
    # canvas.restoreState()
# page_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
# page_template = PageTemplate(id='mypage', frames=[page_frame],
                            #  onPage=header)

# doc.addPageTemplates([page_template])

# Add booking details to the PDF
details_data = [
    ['BOOKING DETAILS FOR', booking_details['name']],
    ['Booking ID:', booking_details['booking_id']],
    ['Name:', booking_details['name']],
    # ['Event Name:', booking_details['event_name']],
    ['Booking date:', booking_details['booking_date']],
    ['Booking slot:', booking_details['booking_slot']],
    ['Adults :',booking_details['Number of adults']],
    ['Children :',booking_details['Number of children']],
    ['Destination:', booking_details['place']],
]
details_table = Table(details_data,colWidths=[doc.width],rowHeights=[22 for i in range(8)])
details_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightskyblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
    ('GRID', (0, 0), (-1, -1), 1, colors.whitesmoke)
]))
elements.append(Image('MHI.png', height=60, width=60 ))
elements.append(details_table)

# Add QR code image to the PDF
qr_code_img = Image(qr_img_path, width=120, height=120)
elements.append(Spacer(0.5, 1))
elements.append(qr_code_img)

# Build the PDF
doc.build(elements)
