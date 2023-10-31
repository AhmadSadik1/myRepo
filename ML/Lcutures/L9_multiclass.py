# %%

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix 
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import seaborn as sn

digits = load_digits()
# dir(digits)

# for i in range(5) :
#     plt.gray()
#     plt.matshow(digits.images[i])

# print(digits.data[0])    
# print(digits.target[0:8])    

# print(digits.data[0:5])
model = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2)

fitting = model.fit(X_train, y_train)

fitting.score(X_test, y_test)

model.predict(digits.data[0:5])

y_predicted = model.predict(X_test)

cm = confusion_matrix(y_test, y_predicted)
cm

plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# %%
