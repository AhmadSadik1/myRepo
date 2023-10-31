from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clfL = GridSearchCV(
    LogisticRegression(solver="liblinear", multi_class="auto"),
    {
        "C": [1, 10, 20],
    },
    cv=5,
    return_train_score=False,
)
clfL.fit(digits.data, digits.target)

clfR = GridSearchCV(
    RandomForestClassifier(),
    {"n_estimators": [1, 5, 10]},
    cv=5,
    return_train_score=False,
)
clfL.fit(digits.data, digits.target)

clfD = GridSearchCV(
    DecisionTreeClassifier(),
    {
        "criterion": ["gini", "entropy"],
    },
    cv= 5 , 
    return_train_score= False
)

clfD.fit(digits.data,  digits.target)
print(clfD.best_params_)
print(clfD.best_score_)
