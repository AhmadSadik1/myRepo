# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# create a numpy array for the input data 'area' and the output data 'price'
area = np.array([[2600 , 3000 , 3200 ,3600 ,4000]]).T  # create a 2D array with a single column
price = np.array([[550000 ,565000, 610000, 680000 , 725000]]).T  # create a 2D array with a single column

# plot the input data
plt.scatter(area ,price , color = 'red' , marker = '+')
plt.xlabel("area")
plt.ylabel("price")

# create a LinearRegression model and fit the data
reg = LinearRegression()
reg.fit(area, price)

# plot the linear regression line
plt.plot(area, reg.predict(area), color='blue')
reg.predict([[3300]])
# print(reg.coef_)
# print(reg.intercept_)




# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# year = np.array([[2010 , 2011 , 2012 ,2013 ,2014 , 2015 , 2016]]).T  
# pci = np.array([[38420.52289 ,42334.71121, 42665.25597, 42676.46837 
#                  , 41039.8936 , 35175.18898 , 34229.19363]]).T  

# plt.xlabel("Year")
# plt.ylabel("pci")
# plt.scatter(year , pci , color = 'red' , marker = '+')

# reg = LinearRegression()
# reg.fit(year , pci)
# plt.plot(year , reg.predict(year) , color = 'blue')
# print(reg.predict([[2020]]))
# %%
