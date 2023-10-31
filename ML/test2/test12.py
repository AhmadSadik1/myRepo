from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets

wine = datasets.load_wine()

X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.2)

model = GaussianNB()
model.fit(X_train , y_train)
print(model.score(X_train , y_train))