import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\salaries.csv")
print(df.head())

data = df.drop(["salary_more_then_100k"], axis="columns")
target = df["salary_more_then_100k"]

le_company = LabelEncoder()
le_job = LabelEncoder()
le_deegree = LabelEncoder()

data["company_n"] = le_company.fit_transform(data["company"])
data["job_n"] = le_job.fit_transform(data["job"])
data["degree_n"] = le_deegree.fit_transform(data["degree"])

clear_data = data[["company_n", "job_n", "degree_n"]]


model  = tree.DecisionTreeClassifier()
fitting = model.fit(clear_data , target)
score = model.score(clear_data , target)
print(model.predict([[2,1,0]]))
