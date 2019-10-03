import numpy as np
import cv2
#ایجاد یک ماتریس سه بعدی طول و عرض 512 و مقدار پیش فرض هر پیکسل ۰
# مقداری که هر پیکسل می گیرد عددی بین ۰ تا ۲۵۵ است
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
#ترسیم خط از دو نقطه
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#ترسیم یک مستطیل
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#ترسیم دایره
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#ترسیم بیضی
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#ثبت متن بر روی تصویر
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
#تابع برای نمایش تصویر استفاده می شود
cv2.imshow('image',img)
#تا زمانی که کلیدی از صفحه کلید زده شود صبر در این خط اجرا می ماند
cv2.waitKey(0)
#پنجره های باز شده توسط این برنامه بسته می شود
cv2.destroyAllWindows()