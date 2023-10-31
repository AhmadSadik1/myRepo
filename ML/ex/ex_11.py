import pandas as pd
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

dig = load_digits()
df = pd.DataFrame(dig.data, dig.target)
df["target"] = dig.target

# X = dig.data
# y = dig.target

X_train, X_test, y_train, y_test = train_test_split(
    df.drop("target", axis="columns"), df.target, test_size=0.3
)

modle = SVC(kernel="linearl")
# modle = SVC(kernel="rbf")
fitting = modle.fit(X_train, y_train)
score = modle.score(X_test, y_test)
print(score)
