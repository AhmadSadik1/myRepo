from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn import linear_model
import pandas as pd


df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\Melbourne_housing_FULL.csv")

cols_to_use = [
    "Suburb",
    "Rooms",
    "Type",
    "Method",
    "SellerG",
    "Regionname",
    "Propertycount",
    "Distance",
    "CouncilArea",
    "Bedroom2",
    "Bathroom",
    "Car",
    "Landsize",
    "BuildingArea",
    "Price",
]
dataset = df[cols_to_use]
dataset.isna().sum()

cols_to_fill_zero = ["Propertycount", "Distance", "Bedroom2", "Bathroom", "Car"]
dataset[cols_to_fill_zero] = dataset[cols_to_fill_zero].fillna(0)

dataset["Landsize"] = dataset["Landsize"].fillna(dataset.Landsize.mean())
dataset["BuildingArea"] = dataset["BuildingArea"].fillna(dataset.BuildingArea.mean())
dataset.dropna(inplace=True)
dataset = pd.get_dummies(dataset, drop_first=True)
X = dataset.drop("Price", axis=1)
y = dataset["Price"]
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=2)
reg = LinearRegression().fit(train_X, train_y)
# * There Is Between trina And test
reg.score(test_X, test_y)
reg.score(train_X, train_y)
# * To Solve This Isuae I Have 2 Way :
# ? L1 :
lasso_reg = linear_model.Lasso(alpha=50, max_iter=100, tol=0.1)
lasso_reg.fit(train_X, train_y)
# * The Differnt has gone .
lasso_reg.score(test_X, test_y)
lasso_reg.score(train_X, train_y)

ridge_reg = Ridge(alpha=50, max_iter=100, tol=0.1)
ridge_reg.fit(train_X, train_y)
# * The Differnt has gone .
ridge_reg.score(test_X, test_y)
ridge_reg.score(train_X, train_y)
