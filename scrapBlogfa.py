#کتابخانه برای پردازش ساختار صفحات وب
import urllib3
from bs4 import BeautifulSoup
import random


def funExtractDate(data_str):
    dayname = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
    yearname = ["۱۳۷", "۱۳۸", "۱۳۹"]
    first_index = -1
    end_index = -1
    for day in dayname:
        first_index = data_str.find(day)
        if first_index > -1:
            break
    print("first insex", first_index)
    for year in yearname:
        end_index = data_str.find(year)
        if end_index > -1:
            break
    print("end insex", end_index)

    if first_index > 0 and end_index > 0:
        print(data_str[first_index:end_index + 4])

def funExtractDivDate(fist_page):
    soup = BeautifulSoup(fist_page, 'html.parser')

    m = soup.find_all("div", class_="postdesc")
    data_str = ""
    if len(m) > 0:
        data_str = m[0].get_text()

    m = soup.find_all("div", class_="postinfo")
    if len(m) > 0:
        data_str = m[0].get_text()

    m = soup.find_all("div", class_="date")
    if len(m) > 0:
        data_str = m[0].get_text()

    m = soup.find_all("div", class_="comment")
    if len(m) > 0:
        data_str = m[0].get_text()

    m = soup.find_all("div", class_="Comment")
    if len(m) > 0:
        data_str = m[0].get_text()
    return data_str

def funExtractBlogLinks(html_page):
    # محتوی صفحه ذخیره شده تحلیل ساختار می شود
    soup = BeautifulSoup(html_page, 'html.parser')
    # لیست تمامی وبلاگ های در یک صفحه خاص استخراج می شود
    infoBarTag = soup.find_all("span", "ur")
    for child in infoBarTag:
        temp = child.get_text()
        print(temp)
        # صفحه اول وبلاگ دریافت می شود
        fist_page = http.request("GET", temp)

        # صفحه اول پردازش می شود و تگ دارای تاریخ پست استخراج می شود
        data_str = funExtractDivDate(fist_page.data)

        # اگر توانست تگ تاریخ را پیدا کند داده های اضافه را از ان جدا کرده تاریخ آخرین پست را چاپ می کند
        if len(data_str) > 0:
            funExtractDate(data_str)
#کتابخانه ای برای ارسال و دریافت درخواست های وب
from urllib.request import urlopen
http = urllib3.PoolManager()


for i in range(5):
    dir=random.randint(1, 12)
    page=random.randint(1, 100)
    print("dir=",dir,"page=",page)
    if dir < 10:
        dir="0"+str(dir)
    url_page="http://blogfa.com/members/userslist.aspx?dir="+str(dir)+"&page="+str(page)
    #لیستی از صفحات وبلاگ ها را دریافت می کند
    html_page =http.request("GET",url_page)
    funExtractBlogLinks(html_page.data)
#print(html_page.data)

    #print(data_str)



