# %%
from sklearn.linear_model import LinearRegression
import matplotlib.pylab as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\canada_per_capita_income.csv")

plt.ylabel("Income")
plt.xlabel("year")
plt.scatter(df["year"], df["per capita income (US$)"], color="red", marker="+")

years = df.year.values.reshape(-1, 1)
model = LinearRegression()
model.fit(df.year.values.reshape(-1, 1), df["per capita income (US$)"])
plt.plot(years, model.predict(years), color="blue")
print(model.predict([[2020]]))


# %%
