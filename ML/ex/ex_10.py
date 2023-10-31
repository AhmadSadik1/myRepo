import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\titanic.csv")

S = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"]

Sex_n = LabelEncoder()
S["Sex_n"] = Sex_n.fit_transform(df.Sex)
S.Age = S.Age.fillna(S.Age.mean())

X = S.drop(["Sex"], axis="columns")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = tree.DecisionTreeClassifier()
fitting = model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(score)
