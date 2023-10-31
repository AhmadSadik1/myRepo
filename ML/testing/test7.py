import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\carprices.csv")

df = df.drop(["Car Model"], axis="columns")

X = df.drop(["Sell Price($)"], axis="columns")
y = df["Sell Price($)"]

X_train, X_test, y_train, y_test = train_test_split(X , y , test_size= 0.3)

reg = LinearRegression()
reg = reg.fit(X_train , y_train)
sor = reg.score(X_test, y_test)  
pre = reg.predict(X_test)    
print(pre)