from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()
df = pd.DataFrame(iris.data, iris.target)

lr = cross_val_score(LogisticRegression(solver='lbfgs', max_iter=1000), iris.data, iris.target)
# np.average(lr)
# print(lr)
svm = cross_val_score(SVC(), iris.data, iris.target)
# np.average(svm)
# print(svm)
dtc = cross_val_score(DecisionTreeClassifier(), iris.data, iris.target)
# np.average(dtc)
# print(dtc)
rfc = cross_val_score(RandomForestClassifier(), iris.data, iris.target)
# np.average(rfc)
# print(rfc)