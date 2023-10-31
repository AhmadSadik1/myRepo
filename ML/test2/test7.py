from sklearn.model_selection import train_test_split 
from sklearn import tree
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\titanic.csv")

df.Sex = df.Sex.map({"male": 1, "female": 2})
df.Age = df.Age.fillna(df.Age.mean())

X = df[["Sex", "Fare", "Pclass", "Age"]]
y = df.Survived

X_train, X_test, y_train, y_test = train_test_split(X , y , test_size= 0.2) 

model = tree.DecisionTreeClassifier()
model.fit(X_train , y_train)
print(model.score(X_test ,y_test))

