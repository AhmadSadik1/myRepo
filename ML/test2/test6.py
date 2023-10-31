# %%
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\HR_comma_sep.csv")

# df.groupby('left').mean()
# pd.crosstab(df.salary,df.left).plot(kind='bar')
# pd.crosstab(df.Department,df.left).plot(kind='bar')

salary = pd.get_dummies(df["salary"], prefix="salary")
df = pd.concat([df, salary], axis="columns")
X = df[
    [
        "satisfaction_level",
        "average_montly_hours",
        "promotion_last_5years",
        "salary_low",
        "salary_medium",
        "salary_high",
    ]
]
y = df["left"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    

model = LogisticRegression(solver='lbfgs', max_iter=100 )
model.fit(X_train , y_train)    
print(model.score(X_test , y_test))

# %%
