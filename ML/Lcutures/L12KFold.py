from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

digits = load_digits()

X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.3
)

# * LogisticRegression
lr = LogisticRegression(solver="liblinear", multi_class="ovr")
lr.fit(X_train, y_train)
lr.score(X_test, y_test)

# * SVM
svm = SVC(gamma="auto")
svm.fit(X_train, y_train)
svm.score(X_test, y_test)

# * Random Forest
rf = RandomForestClassifier(n_estimators=40)
rf.fit(X_train, y_train)
rf.score(X_test, y_test)

# * 3 Fild .
kf = KFold(n_splits=3)
for train_index, test_index in kf.split([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    # print(train_index, test_index)
    pass

# ? Output 
# * Look Here
# * First trin 3 ,4 ,... And test 0 ,1 ,2
# * secound trin 1 ,2 ,... And test 3 ,4 ,5
# [3 4 5 6 7 8] [0 1 2]
# [0 1 2 6 7 8] [3 4 5]
# [0 1 2 3 4 5] [6 7 8]


def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)


# ! I Can Replace This Line In Libary In sk .
# * Here We Use StratifiedKFold
folds = StratifiedKFold(n_splits=3)

scores_logistic = []
scores_svm = []
scores_rf = []

for train_index, test_index in folds.split(digits.data,digits.target):
    X_train, X_test, y_train, y_test = digits.data[train_index], digits.data[test_index], \
                                       digits.target[train_index], digits.target[test_index]
    scores_logistic.append(get_score(LogisticRegression(solver='liblinear',multi_class='ovr'), X_train, X_test, y_train, y_test))  
    scores_svm.append(get_score(SVC(gamma='auto'), X_train, X_test, y_train, y_test))
    scores_rf.append(get_score(RandomForestClassifier(n_estimators=40), X_train, X_test, y_train, y_test))

print(scores_logistic)
# ? OutPut
# * [0.8953488372093024, 0.9499165275459098, 0.9093959731543624]
# print(scores_svm)
# ? OutPut 
# * [0.39368770764119604, 0.41068447412353926, 0.4597315436241611]
# print(scores_rf)
# ? OutPut  
# * [0.9285714285714286, 0.9515859766277128, 0.9295302013422819]

# ! Here The Libary
lg = cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr') , digits.data , digits.target)
# ? OutPut 
#* array([0.89534884, 0.94991653, 0.90939597])

svc =cross_val_score(SVC(gamma='auto'), digits.data, digits.target,cv=3)
# ? OutPut 
# * array([0.93521595, 0.94156928, 0.93288591])

# * I Can Here Chnage The n_estimatiors .
rm = cross_val_score(RandomForestClassifier(n_estimators=40),digits.data, digits.target,cv=3)
# ? OutPut
# * array([0.93521595, 0.94156928, 0.93288591])
