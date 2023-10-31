# %%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import pandas as pd

dataset = load_digits()


# * Here I Have 64 col
dataset.data.shape

dataset.data[0].reshape(8, 8)
plt.gray()
plt.matshow(dataset.data[0].reshape(8, 8))

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

X = df
y = dataset.target

# ! The diffrent between standerscaler and pca :
# In general, StandardScaler should be used before PCA
# This is because PCA works best when the features are on a similar scale.
# If the features are not on a similar scale, PCA will be biased towards the features with larger variances.
X_scaler = StandardScaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaler, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)
model.score(X_test, y_test)

pca = PCA(0.95)
pca = pca.fit_transform(X)

pca.shape
pca.explained_variance_ratio_
pca.n_components_

X_train_pca, X_test_pca, y_train, y_test = train_test_split(
    pca, y, test_size=0.2, random_state=30
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
X_pca.shape

X_train_pca, X_test_pca, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.2, random_state=30
)
# * You Can See Here How socre Is Low .
model = LogisticRegression(max_iter=1000)
model.fit(X_train_pca, y_train)
model.score(X_test_pca, y_test)
