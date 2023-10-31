# %%
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.drop(["sepal length (cm)", "sepal width (cm)"], axis="columns", inplace=True)


# plt.scatter(df["petal length (cm)"], df["petal width (cm)"])
# plt.xlabel("Age")
# plt.ylabel("Income($)")

km = KMeans(n_clusters=3)
per = km.fit_predict(df[["petal length (cm)", "petal width (cm)"]])
df["cluster"] = per

df0 = df[df["cluster"] == 0]
df1 = df[df["cluster"] == 1]
df2 = df[df["cluster"] == 2]
# plt.scatter(df0["petal length (cm)"], df0["petal width (cm)"], color="blue")
# plt.scatter(df1["petal length (cm)"], df1["petal width (cm)"], color="green")
# plt.scatter(df2["petal length (cm)"], df2["petal width (cm)"], color="yellow")

# scaler = MinMaxScaler()

# scaler.fit(df[["petal length (cm)"]])
# df["petal length (cm)"] = scaler.transform(df[["petal length (cm)"]])

# scaler.fit(df[["petal width (cm)"]])
# df["petal width (cm)"] = scaler.transform(df[["petal width (cm)"]])


arr = []
ranges = range(1, 10)

for k in ranges :
    ss = KMeans(n_clusters=k)
    ss.fit(df)
    arr.append(ss.inertia_) 

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(ranges,arr) 

# %%
