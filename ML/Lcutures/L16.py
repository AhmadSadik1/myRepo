from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressi
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import svm, datasets
import pandas as pd

iris = datasets.load_iris()

# ? Approach 1: Use train_test_split and manually tune parameters by trial and error
# X_train, X_test, y_train, y_test = train_test_split(iris.data , iris.target , test_size= 0.2)
# model = svm.SVC(kernel='rbf',C=30,gamma='auto')
# model.fit(X_train,y_train)
# model.score(X_test, y_test)

# ? Approach 2: Use K Fold Cross validation
# Manually try suppling models with different parameters to cross_val_score function with 5 fold cross validation
# cross_val_score(svm.SVC(kernel='linear',C=10,gamma='auto'),iris.data, iris.target, cv=5) array([1.        , 1.        , 0.9       , 0.96666667, 1.        ])
# cross_val_score(svm.SVC(kernel='rbf',C=10,gamma='auto'),iris.data, iris.target, cv=5)  array([0.96666667, 1.        , 0.96666667, 0.96666667, 1.        ])
# cross_val_score(svm.SVC(kernel='rbf',C=20,gamma='auto'),iris.data, iris.target, cv=5) array([0.96666667, 1.        , 0.9       , 0.96666667, 1.        ])

# ? Above approach is tiresome and very manual. We can use for loop as an alternative
# kernels = ['rbf', 'linear']
# C = [1,10,20]
# avg_scores = {}
# for kval in kernels:
#     for cval in C:
#         cv_scores = cross_val_score(svm.SVC(kernel=kval,C=cval,gamma='auto'),iris.data, iris.target, cv=5)
#         avg_scores[kval + '_' + str(cval)] = np.average(cv_scores)

# avg_scores

# ? Approach 3: Use GridSearchCV

# clf = GridSearchCV(
#     svm.SVC(gamma="auto"),
#     {"C": [1, 10, 20], "kernel": ["rbf", "linear"]},
#     cv=5,     
#     return_train_score=False,
# )
# clf.fit(iris.data, iris.target)
#  print(clf.cv_results_)
# df = pd.DataFrame(clf.cv_results_)
# print(df[["param_C", "param_kernel", "mean_test_score"]])
# print(clf.best_params_)
# print(clf.best_score_)

# from sklearn.model_selection import RandomizedSearchCV
# rs = RandomizedSearchCV(svm.SVC(gamma='auto'), {
#         'C': [1,10,20],
#         'kernel': ['rbf','linear']
#     },
#     cv=5,
#     return_train_score=False,
#     n_iter=2
# )
# rs.fit(iris.data, iris.target)
# pd.DataFrame(rs.cv_results_)[['param_C','param_kernel','mean_test_score']]

# ? To Choses Best Model .
# model_params = {
#     'svm': {
#         'model': svm.SVC(gamma='auto'),
#         'params' : {
#             'C': [1,10,20],
#             'kernel': ['rbf','linear']
#         }  
#     },
#     'random_forest': {
#         'model': RandomForestClassifier(),
#         'params' : {
#             'n_estimators': [1,5,10]
#         }
#     },
#     'logistic_regression' : {
#         'model': LogisticRegression(solver='liblinear',multi_class='auto'),
#         'params': {
#             'C': [1,5,10]
#         }
#     },
#     'naive_bayes_gaussian': {
#         'model': GaussianNB(),
#         'params': {}
#     },
#     'naive_bayes_multinomial': {
#         'model': MultinomialNB(),
#         'params': {}
#     },
#     'decision_tree': {
#         'model': DecisionTreeClassifier(),
#         'params': {
#             'criterion': ['gini','entropy'],
            
#         }
#     }     
# }

# scores = []

# for model_name, mp in model_params.items():
#     clf =  GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
#     clf.fit(iris.data, iris.target)
#     scores.append({
#         'model': model_name,
#         'best_score': clf.best_score_,
#         'best_params': clf.best_params_
#     })

# df = pd.DataFrame(scores,columns=['model','best_score','best_params'])
# df
