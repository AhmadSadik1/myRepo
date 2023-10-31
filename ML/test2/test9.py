from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)

model = RandomForestClassifier(n_estimators=10)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
