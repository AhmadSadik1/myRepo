# %%
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'C:\Users\Ahmad\Desktop\exfile\canada_per_capita_income.csv') 

plt.plot(df.year , df['per capita income (US$)'])
plt.xlabel('Year')
plt.ylabel('Income')

reg = LinearRegression()
reg.fit(df[['year']] , df['per capita income (US$)'])    
print(reg.predict([[2020]]))

# %%
