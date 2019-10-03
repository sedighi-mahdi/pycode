import mysql.connector
# تابع برای برقرار اتصال به بانک داده استفاده می شود
mydb = mysql.connector.connect(
  host="localhost",  #  نام یا ای پی سیستمی که بانک داده بر روی ان قرار دارد
  user="root",       #  نام کاربری برای اتصال
  passwd="root",     #  رمز عبور برای اتصال
  database='test'    #  نام بانک داده
)

#  ایجاد یک کرسر از روی اتصال برقراری
mycursor = mydb.cursor()
sql = "INSERT INTO tbl_test (`test_title`, `test_course`) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
#اجرا کوئری
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#تابع زیر یک کوئری را دریافت کرده بر روی بانک داده اجرا می کند
mycursor.execute("SELECT * FROM tbl_test")
#تابع زیر همه رکورد ها را خوانده درون متغییر قرار می دهد
myresult = mycursor.fetchall()
#درون حلقه نتیجه های ذخیره شده پیمایش می شود و چاپ می گردد
for x in myresult:
  print(x)



