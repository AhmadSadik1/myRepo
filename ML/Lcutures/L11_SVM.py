# %%

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = load_iris()

df = pd.DataFrame(iris["data"], columns=iris["feature_names"]) 

df["target"] = iris.target
df["target_name"] = df.target.apply(lambda x: iris.target_names[x])


df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

# * Noties Here I Can Draw A Line In Miiddel .
plt.scatter(df0["sepal length (cm)"], df0["sepal width (cm)"], color="red", marker="+")
plt.scatter(df1["sepal length (cm)"], df1["sepal width (cm)"], color="blue", marker=".")

X = df.drop(["target", "target_name"], axis="columns")
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# * If You Print 'modle' You Can See Value Like 'c' ...
# * You Can Edit This Value .
model = SVC()
fitting = model.fit(X_train, y_train)
scor = model.score(X_test, y_test)


# %%
