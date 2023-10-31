from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.svm import SVC

digits = load_digits()
import pandas as pd

df = pd.DataFrame(digits.data, digits.target)
df["target"] = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    df.drop("target", axis="columns"), df.target, test_size=0.3
)


# model = SVC(kernel="rbf")
# model = SVC(kernel='linear')
model = SVC(C= 10)
model.fit(X_train , y_train)    
print(model.score(X_test , y_test))