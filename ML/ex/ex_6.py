import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\carprices.csv")

model = pd.get_dummies(df["Car Model"])
cont = pd.concat([model, df], axis="columns")

drops = cont.drop(["Car Model"], axis="columns")
drops = drops.drop(["Mercedez Benz C class"], axis="columns")

x = drops.drop(["Sell Price($)"], axis="columns")
y = drops["Sell Price($)"]

reg = LinearRegression()
reg = reg.fit(x, y)
reg = reg.score(x, y)
reg = reg.predict([[0, 1, 86000, 7]])

print(reg)
