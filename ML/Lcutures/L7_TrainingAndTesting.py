# %%

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\carprices.csv")

df = df.drop(["Car Model"], axis="columns")

plts = plt.scatter(df["Mileage"], df["Sell Price($)"])
plts = plt.scatter(df["Age(yrs)"], df["Sell Price($)"])

x = df.drop(["Sell Price($)"], axis="columns")
y = df["Sell Price($)"]

# Train-test split is a technique used to evaluate the performance of machine learning models.
# It involves splitting the dataset into two parts: a training set and a testing set. The training set is
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=10)


reg = LinearRegression()
reg = reg.fit(x_train, y_train)
score = reg.score(x_test, y_test)
reg = reg.predict(x_test, y_test)
print(score)
print(reg)

# %%
