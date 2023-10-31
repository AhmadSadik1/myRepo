# %%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pylab as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\carprices.csv")

# plt.scatter(df["Mileage"], df["Sell Price($)"], color="red", marker="+")



X = df[['Mileage','Age(yrs)']]
y = df["Sell Price($)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train , y_train)
print(model.score(X_test , y_test))
plt.scatter(df["Sell Price($)"] , model.predict(X_test))

# %%
