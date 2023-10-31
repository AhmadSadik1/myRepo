import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'area': [2600, 3000, 3200, 3600, 4000],
        'bedroom': [3, 4, 3, 3, 5],
        'age': [20, 15, 18, 30, 8],
        'price': [550000, 565000, 610000, 595000, 760000]}
df = pd.DataFrame(data)

# create the input features matrix X and the target variable y
X = df[['area', 'bedroom', 'age']]
y = df['price']

# create a linear regression model and fit it to the data
reg = LinearRegression()
reg.fit(X, y)

reg.predict([[3000 , 3 , 40]])