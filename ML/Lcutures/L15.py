from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\spam.csv")

df["spam"] = df["Category"].apply(lambda x: 1 if x == "spam" else 0)

X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam)

v = CountVectorizer()

X_train_count = v.fit_transform(X_train.values)
X_test_count = v.transform(X_test.values)  # Use transform instead of fit_transform
# * Like Matrix
X_train_count.toarray()[:2]

model = MultinomialNB()
model.fit(X_train_count, y_train)

emails = [
    "Hey mohan, can we get together to watch football game tomorrow?",
    "Up to 20% discount on parking, exclusive offer just for you. Don't miss this reward!",
]
emails_count = v.transform(emails)  # Use the same vectorizer for transforming
# print(model.predict(emails_count))

score = model.score(X_test_count, y_test)
print(score)

# ! I Can Use This Way Rather Then Over X_train_count = v.fit_transform(X_train.values) ..

# clf = Pipeline([
#     ('vectorizer', CountVectorizer()),
#     ('nb', MultinomialNB())
# ])

# clf.fit(X_train, y_train)
# clf.score(X_test,y_test)
# clf.predict(emails)