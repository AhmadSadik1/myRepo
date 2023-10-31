from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['flower'] = iris.target
df.drop(['sepal length (cm)', 'sepal width (cm)', 'flower'],axis='columns',inplace=True)


k = KMeans(n_clusters=3)    
y_pre = k.fit_predict(df)

df['cluster'] = y_pre