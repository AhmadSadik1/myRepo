from sklearn.linear_model import LinearRegression
from word2number import w2n
import pandas as pd 
import math
df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\hiring1.csv")

df['experience'] = df['experience'].fillna("zero")

df['experience'] = df['experience'].apply(w2n.word_to_num)

median_test_score = math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(median_test_score)

x = df[['experience' , 'test_score(out of 10)' , 'interview_score(out of 10)']]
y = df['salary($)']

model = LinearRegression()
model.fit(x , y) 
print(model.predict([[2,9,6]]))
