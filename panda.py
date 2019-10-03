import pandas as pd


data = pd.read_csv("state.csv")

# ده رکورد اول لیست را در خروجی چاپ می کند
print("Head -- \n", data.head(10))

# ده رکورد آخر داده را در خروجی چاپ می کند
print("\n\n Tail -- \n", data.tail(10))

#نسبت جمعتی به میلیون نفر
data['PopulationInMillions'] = data['Population']/1000000
print (data.head(5))

#تحلیلی بر روی همه ستون های داده انجام می دهد
data.describe()

#میانگین ستون نرخ قتل را محاسبه و چاپ می کند
MurderRate_mean = data.MurderRate.mean()
print("\nMurderRate Mean : ", MurderRate_mean)

#میانه ستون جمعیت را بدست آورده و چاپ می کند
Population_median = data.Population.median()
print("Population median : ", Population_median)

MurderRate_median = data.MurderRate.median()
print("\nMurderRate median : ", MurderRate_median)

