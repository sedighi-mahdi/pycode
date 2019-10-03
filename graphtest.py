import matplotlib.pyplot as plt

# x مقادیر محور
x = [1, 2, 3, 4, 5, 6]
# مقادیر محور
y = [2, 4, 1, 5, 2, 6]

# ترسیم نقاط
plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
# تنظیم حدود هر محور
plt.ylim(1, 8)
plt.xlim(1, 8)
# برچسب گذاری محورها
plt.xlabel('x - axis')

plt.ylabel('y - axis')

# عنوان محور
plt.title('Some cool customizations!')

# نمایش محور
plt.show()

