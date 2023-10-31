import pandas as pd
from word2number import w2n
import math
from sklearn import linear_model

d = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\hiring.csv")
# print(d.head())

d.experience = d.experience.fillna("zero")
d.experience = d.experience.apply(w2n.word_to_num)
median_test_score = math.floor(d['test_score(out of 10)'].mean())
d['test_score(out of 10)'] = d['test_score(out of 10)'].fillna(median_test_score)
reg = linear_model.LinearRegression()
reg.fit(d[['experience','test_score(out of 10)','interview_score(out of 10)']],d['salary($)'])
news = reg.predict([[2,9,6]])
# print(d)