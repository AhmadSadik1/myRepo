from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\carprices.csv")

dummy = pd.get_dummies(df["Car Model"])

df = pd.concat([df, dummy], axis="columns")
df = df.drop(["Mercedez Benz C class", "Car Model"], axis="columns")

X = df.drop(["Sell Price($)"], axis="columns")
y = df["Sell Price($)"]

model = LinearRegression()
model.fit(X , y)    
print(model.score(X ,y))
print(model.predict([[45000,4,0,0]]))