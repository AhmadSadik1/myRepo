from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
import pickle
import json

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\Bengaluru_House_Data.csv")
# print(df.head())
df = df.drop(["area_type" , "availability","society", "balcony"], axis="columns")
# print(df.columns[df.isna().any()])
#* 'location', 'size', 'bath'
# print(df.head())
# print(df['price'].isna().sum()) 

# print(len(df["location"].unique()))


dummy = pd.get_dummies(df.location)
df = pd.concat([df, dummy], axis="columns")

# print(df['bath'].isna().sum()) 

df = df.dropna()

df["bhk"] = df["size"].apply(lambda x: int(x.split(" ")[0]))
df = df.drop(["location" ,"size"] , axis= "columns")

# ToDo  Fix totla_sqft


def preprocess_sqft(sqft):
    parts = sqft.split('-')
    if len(parts) == 2:
        return (float(parts[0]) + float(parts[1])) / 2
    try:
        return float(sqft)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(preprocess_sqft)

df = df[df.bath < df.bhk + 2]

