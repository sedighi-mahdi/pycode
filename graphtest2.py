import matplotlib.pyplot as plt

# مختصاتی که هر میله در آن قرار می گیرد
left = [1, 2, 3, 4, 5]

# ارتفاع هر میله
height = [10, 24, 36, 40, 5]

# عنوان هر میله
tick_label = ['one', 'two', 'three', 'four', 'five']

# ترسیم میله ها
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# برچسب محورها
plt.xlabel('x - axis')

plt.ylabel('y - axis')
# عنوان نمودار
plt.title('My bar chart!')

# ترسیم نمودار
plt.show()


