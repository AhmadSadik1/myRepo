import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\carprices.csv")

dumy = pd.get_dummies(df["Car Model"])
finall = pd.concat([df, dumy], axis="columns")
merigd = finall.drop(["Car Model", "Mercedez Benz C class"], axis="columns")

X = merigd.drop(["Sell Price($)"], axis="columns")
y = merigd["Sell Price($)"]

reg = LinearRegression()

reg.fit(X, y)
soso = reg.score(X, y)
print(reg.predict([[45000, 4, 0, 0]]))
print(reg.predict([[86000, 7, 0, 1]]))
