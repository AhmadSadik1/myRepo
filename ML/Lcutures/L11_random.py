from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data , iris.target , test_size= 0.2)

model = RandomForestClassifier(n_estimators=30)
fitting = model.fit(X_train , y_train)
score = fitting.score(X_test , y_test)
print(score)
