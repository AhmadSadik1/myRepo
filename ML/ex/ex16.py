from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn import svm
import pandas as pd

digits = datasets.load_digits()

model_params = {
    "svm": {
        "model": svm.SVC(gamma="auto"),
        "params": {"C": [1, 10, 20], "kernel": ["rbf", "linear"]},
    },
    "random_forest": {
        "model": RandomForestClassifier(),
        "params": {"n_estimators": [1, 5, 10]},
    },
    "logistic_regression": {
        "model": LogisticRegression(solver="liblinear", multi_class="auto"),
        "params": {"C": [1, 5, 10]},
    },
    "naive_bayes_gaussian": {"model": GaussianNB(), "params": {}},
    "naive_bayes_multinomial": {"model": MultinomialNB(), "params": {}},
    "decision_tree": {
        "model": DecisionTreeClassifier(),
        "params": {
            "criterion": ["gini", "entropy"],
        },
    },
}

scores = []

for model_name, mp in model_params.items():
    clf = GridSearchCV(mp["model"], mp["params"], cv=5, return_train_score=False)
    clf.fit(digits.data, digits.target)
    scores.append(
        {
            "model": model_name,
            "best_score": clf.best_score_,
            "best_params": clf.best_params_,
        }
    )

df = pd.DataFrame(scores, columns=["model", "best_params", "best_score"])
print(df)
