# %%
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits 
import matplotlib.pyplot as plt
import seaborn as sn


digits = load_digits()

X_train, X_test, y_train, y_test = train_test_split(digits.data , digits.target , test_size= 0.2) 
model = RandomForestClassifier(n_estimators= 20)
fitting = model.fit(X_train , y_train)
score = model.score(X_test , y_test)
# print(score)

y_predicted = model.predict(X_test)
cm = confusion_matrix(y_test, y_predicted)
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')


# %%
