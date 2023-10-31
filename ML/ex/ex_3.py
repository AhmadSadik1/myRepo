import pandas as pd
from sklearn.linear_model import LinearRegression
from word2number import w2n
import math


df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\hiringex.csv")

df.experience = df.experience.fillna("zero")
df.experience = df.experience.apply(w2n.word_to_num)

test = math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(test)

X = df[['experience','test_score(out of 10)','interview_score(out of 10)']]
y = df['salary($)']


reg = LinearRegression()
fitting = reg.fit(X , y )


print(fitting.predict([[2,9,6]]))
print(reg.predict([[12,10,10]]))