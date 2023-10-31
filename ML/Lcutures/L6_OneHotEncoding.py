import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\homeprices.csv")
# print(df)

dummy = pd.get_dummies(df.town)
merged = pd.concat([df, dummy], axis="columns")
finall = merged.drop(["town", "west windsor"], axis="columns")

x = finall.drop(["price"], axis="columns")
y = finall.price

reg = LinearRegression()
reg.fit(x, y)
reuslt = reg.predict(x)
things = reg.score(x, y)
print(things)
reuslt = reg.predict([[2800, 0, 1]])
# print(reuslt)
