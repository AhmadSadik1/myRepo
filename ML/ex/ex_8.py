# %%
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\HR_comma_sep.csv")


subdf  = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]

salary_dummies = pd.get_dummies(subdf.salary, prefix="salary")
df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')
df_with_dummies.drop('salary',axis='columns',inplace=True)
X = df_with_dummies

left = df[df.left == 0]
# print(left.shape)

retained = df[df.left == 1]
# print(retained.shape)

mean = df.groupby('left').mean(numeric_only=True)
# print(mean)

# pd.crosstab(df.salary,df.left).plot(kind='bar')

# pd.crosstab(df.Department , df.left).plot(kind='bar')


y = df.left

reg = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(X , y , train_size= 0.3)

reg.fit(X_train, y_train)

reg.score(X_test,y_test)


# %%
