
import pandas as pd

import matplotlib.pyplot as plt


plt.style.use("fivethirtyeight")


# Data :
    
data = pd.read_excel("/storage/emulated/0/Python Projects/Matplotlib/Matplotlib Line Chart/Country's Population Growth Comparison/Population Growth.xlsx")


# Assigning data :

us = data[data.Country == "United States"]

china = data[data.Country == "China"]

india = data[data.Country == "India"]

uk = data[data.Country == "United Kingdom"]


# Ploting Line graph :
    
plt.plot(us.Year, us.Population / 10**6, label = "United States", color = "green")

plt.plot(china.Year, china.Population / 10**6, label = "China")

plt.plot(india.Year, india.Population / 10**6, label = "India")

plt.plot(uk.Year, uk.Population / 10**6, label = "United Kingdome")

# Labeling :
    
plt.title("Country's Population Growth By Year (in million)")

plt.legend()

plt.xlabel("Year >>> ")

plt.ylabel("Population >>> ")

plt.tight_layout()

plt.show()

''' Created By Sourin Das '''
