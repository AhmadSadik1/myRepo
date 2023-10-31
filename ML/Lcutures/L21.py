from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\pima-indians-diabetes.csv")

# print(df.isnull().sum())
# print(df.describe())
# * This Is My Target :
# * And From Here You See
# 0 : 500
# 1 : 268
# * There are not much imbalance
# print(df.Outcome.value_counts())

X = df.drop("Outcome", axis="columns")
y = df.Outcome

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled[:3]


X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, stratify=y, random_state=10
)
# * So See Here The Output
# 0 : 375
# 1 : 201
# print(y_train.value_counts())

# clss = cross_val_score(DecisionTreeClassifier(), X, y, cv=5)
# clss.mean()

# Train using Bagging

# bag = BaggingClassifier(
#     base_estimator=DecisionTreeClassifier(),
#     n_estimators=100,
#     max_samples=0.8,
#     oob_score=True,
#     random_state=0,
# )
# bag.fit(X_train, y_train)
# bag.oob_score_


# bag_model = BaggingClassifier(
#     base_estimator=DecisionTreeClassifier(),
#     n_estimators=100,
#     max_samples=0.8,
#     oob_score=True,
#     random_state=0
# )
# scores = cross_val_score(bag_model, X, y, cv=5)


# scores = cross_val_score(RandomForestClassifier(n_estimators=50), X, y, cv=5)
# scores.mean()