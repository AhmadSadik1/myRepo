import pandas as pd
from word2number import w2n
import math
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\hiring1.csv")
df.experience = df.experience.fillna("zero")
df["test_score(out of 10)"] = df["test_score(out of 10)"].fillna(0)
df.experience = df.experience.apply(w2n.word_to_num)

dfs = math.floor(df["test_score(out of 10)"].mean())
df["test_score(out of 10)"] = df["test_score(out of 10)"].fillna(dfs)

X = df[["experience", "test_score(out of 10)", "interview_score(out of 10)"]]
y = df["salary($)"]

reg = LinearRegression()
reg.fit(X, y)
print(reg.predict([[12, 10, 10]]))
