from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\titanic1.csv")
df.drop(
    ["PassengerId", "Name", "SibSp", "Parch", "Ticket", "Cabin", "Embarked"],
    axis="columns",
    inplace=True,
)

inputs = df.drop(["Survived"], axis="columns")
target = df["Survived"]

dummy = pd.get_dummies(df["Sex"])
inputs = pd.concat([inputs, dummy], axis="columns")

inputs = inputs.drop(["Sex"], axis="columns")

isany = inputs.columns[inputs.isna().any()]

inputs.Age = inputs.Age.fillna(inputs.Age.mean())

X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)

model = GaussianNB()
model.fit(X_train,y_train)
socre = model.score(X_test , y_test)
print(socre)
