import matplotlib.pyplot as plt

# گروه ها
activities = ['eat', 'sleep', 'work', 'play']

# سهم هر گروه به ترتیب
slices = [3, 7, 8, 6]

# رنگ مورد استفاده برای هر گروه
colors = ['r', 'y', 'g', 'b']

# ترسیم نودار دایره ای
plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True, radius=1.2)

# plotting legend
plt.legend()

# showing the plot
plt.show()

