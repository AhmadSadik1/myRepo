from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np


iris = load_iris()

l_scores = cross_val_score(LogisticRegression(), iris.data, iris.target)
d_scores = cross_val_score(DecisionTreeClassifier(), iris.data, iris.target)
s_scores = cross_val_score(SVC(), iris.data, iris.target)
r_scores = cross_val_score(RandomForestClassifier(n_estimators=40), iris.data, iris.target)

print(np.average(l_scores))
print(np.average(d_scores))
print(np.average(s_scores))
print(np.average(r_scores))




