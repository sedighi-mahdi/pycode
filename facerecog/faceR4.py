# ایمپورت کردن کتابخانه های مورد نیاز
import os
import face_recognition

# لیست تمامی تصاویر را در متغییر قرار می دهد
images = os.listdir('images')

# تصویر که می خواهیم در بانک جستجو کنیم
image_to_be_matched = face_recognition.load_image_file('alidoost1.jpeg')

# بردار ویژگی تصویری مورد جستجو را استخراج کرده در متغییر قرار می دهیم
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]

# درون حلقه تصویر مورد جستجو را با تک تک تصاویر مقایسه می کنیم
# در صورتی که قابل با تصویر منطبق بود پیام   چاپ می شود
for image in images:
    # یکی از تصاویر پوشه لود می شود
    current_image = face_recognition.load_image_file("images/" + image)
    # بردار ویژگی آن استخراج می شود
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # تصویر مورد نظر با تصویر جاری مقایسه می شود
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # در صورت مطابقت یا عدم مطابقت پیام مورد نظر چاپ خواهد شد
    if result[0] == True:
        print("Matched: " + image)
    else:
        print("Not matched: " + image)

