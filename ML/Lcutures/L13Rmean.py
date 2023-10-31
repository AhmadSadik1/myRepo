# %%
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\income3.csv")

# plt.scatter(df.Age, df["Income($)"])
# plt.xlabel("Age")
# plt.ylabel("Income($)")

km = KMeans(n_clusters=3)
y_pre = km.fit_predict(df[["Age", "Income($)"]])
df['cluster']=y_pre

# df0 = df[df.cluster == 0]
# df1 = df[df.cluster == 1]
# df2 = df[df.cluster == 2]
# ! Noties Here There Worng I Draw 
# plt.scatter(df0.Age,df0['Income($)'],color='green')
# plt.scatter(df1.Age,df1['Income($)'],color='red')
# plt.scatter(df2.Age,df2['Income($)'],color='black')
# plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
# plt.xlabel('Age')
# plt.ylabel('Income ($)')
# plt.legend()

# ! Fix Darw 

scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
df['clusters']=y_predicted


# df1 = df[df.clusters==0]
# df2 = df[df.clusters==1]
# df3 = df[df.clusters==2]
# plt.scatter(df1.Age,df1['Income($)'],color='green')
# plt.scatter(df2.Age,df2['Income($)'],color='red')
# plt.scatter(df3.Age,df3['Income($)'],color='black')
# plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
# plt.legend()

k_rng = range(1,10)
sse = []
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)


plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)
# %%
