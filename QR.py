# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = "صادق چاجی\r\n کارشناس شبکه\r\n معاونت آمار و فناوری اطلاعات"
  
# Generate QR code 
url = pyqrcode.create(s, encoding='utf-8') 
  
# Create and save the png file naming "myqr.png" 
url.svg("myqr1.svg", scale = 8) 

