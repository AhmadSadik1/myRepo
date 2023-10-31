from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
import matplotlib.pylab as plt
import seaborn as sn

ld = load_digits()

X_train, X_test, y_train, y_test = train_test_split(
    ld.data, ld.target, test_size=0.3, random_state=10
)

clf = GridSearchCV(
    KNeighborsClassifier(),
    {"n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    return_train_score=False,
    cv=3
)
# model = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)
df = ld.DataFrame(clf.cv_results_)
print(df[["param_C", "param_kernel", "mean_test_score"]])
print(clf.best_params_)
print(clf.best_score_)


# y_pred = model.predict(X_test)
# cm = confusion_matrix(y_test, y_pred)

# plt.figure(figsize=(7, 5))
# sn.heatmap(cm, annot=True)
# plt.xlabel("Predicted")
# plt.ylabel("Truth")