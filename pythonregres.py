import numpy as np
import matplotlib.pyplot as plt
# تعداد نقاط مورد نظر برای نمونه گیری
numPoint=20
# استخراج چند داده تصادفی و مرتب کردن انها
x=7*np.random.rand(numPoint)
x=np.sort(x)
# ایجاد نویز نرمال
noise=np.random.normal(0 , 0.1 , numPoint)
#ایجاد تابع y
y=np.sin(x)
#اضافه کردن نویز به داده ها
ynoise=y+noise

# تخمین یک تابع مرتبه ۳ با داده های موجود
z = np.polyfit(x, ynoise, 3)
# ضرایب چند جمله ای تخمین زده شده
p = np.poly1d(z)
# مقادیر تخمین زده توسط چند جمله ای
yest=p(x)

# ترسیم نمودار اصلی
plt.plot(x, y, color='green', linewidth=3,)
# ترسیم نمودار با داده های دارای نویز
plt.plot(x, ynoise, color='red', linestyle='dashed', linewidth=3,
         marker='*', markerfacecolor='blue', markersize=6)
#ترسیم نمودار با چند جمله برازش شده
plt.plot(x, yest, color='blue', linestyle='dashed',)
plt.show()



