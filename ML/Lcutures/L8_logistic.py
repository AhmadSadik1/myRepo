# %%

import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# df.groupby('left').mean()
df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\insurance_data.csv")
print(df.head())
plts = plt.scatter(df.age, df.bought_insurance, marker='+', color='red')

X_train, X_test, y_train, y_test = train_test_split(
    df[['age']], df.bought_insurance, train_size=0.8)


reg = LogisticRegression()
reg = reg.fit(X_train , y_train)
per = reg.predict(X_test)
scor = reg.score(X_test , y_test)
proba = reg.predict_proba(X_test)

# print(proba)



# %%
