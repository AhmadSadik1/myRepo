# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\HR_comma_sep.csv")
pd.crosstab(df.salary,df.left).plot(kind='bar')
plt.xlabel("salary")
plt.ylabel("left")

subdf = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
salary_dummies = pd.get_dummies(subdf.salary, prefix="salary")
df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')
df_with_dummies.drop('salary',axis='columns',inplace=True)
X = df_with_dummies
y = df.left

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

reg = LogisticRegression()
reg = reg.fit(X_train , y_train)
pre = reg.predict(X_test)
print(pre)
scor = reg.score(X_test , y_test)
print(scor)


# %%
