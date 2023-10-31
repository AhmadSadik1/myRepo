from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets

wine = datasets.load_wine()

X_train, X_test, y_train, y_test = train_test_split(wine.data , wine.target , test_size= 0.2)   

model = GaussianNB()
model.fit(X_train , y_train)
score = model.score(X_test , y_test)

mn = MultinomialNB()
mn.fit(X_train,y_train)
scores = mn.score(X_test,y_test)
print(scores)