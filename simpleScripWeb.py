#کتابخانه برای پردازش ساختار صفحات وب
from bs4 import BeautifulSoup 
#کتابخانه ای برای ارسال و دریافت درخواست های وب
from urllib.request import urlopen

#با استفاده از تابع زیر آدرس داده شده را ذخیره کرد 
html_page = urlopen("http://www.tgju.org/dollar-chart")

# محتوی صفحه ذخیره شده تحلیل ساختار می شود
soup = BeautifulSoup(html_page, 'html.parser')
# با استفاده از تابع زیر می توان تمام عناصر ul 
#با کلاس داده شده را جستجو کرد
infoBarTag=soup.find('ul', class_="info-bar")


for child in infoBarTag.children:
    temp=child.find('span', class_="info-price")
    print(temp.get_text())
    

