
import pandas as pd

import matplotlib.pyplot as plt


plt.style.use("fivethirtyeight")


# Data :
    
data = pd.read_excel("https://github.com/SourinDaz/Most-Popular-Programing-Language/blob/3faec0dc1d9f2d9cf5bc418066efd4580b3202f1/Population%20Growth.xlsx")


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
