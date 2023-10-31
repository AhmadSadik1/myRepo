from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import tensorflow as tf
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\Churn_Modelling.csv")

df = df.drop("RowNumber", axis="columns")
df = df.drop("CustomerId", axis="columns")
df = df.drop("Surname", axis="columns")


def print_object(df):
    for column in df:
        if df[column].dtype == "object":
            print(f"{column} : {df[column].unique()}")


df["Gender"].replace({"Female": 1, "Male": 0}, inplace=True)

df = pd.get_dummies(data=df, columns=["Geography"])

cols_to_scale = ["CreditScore", "Age", "Tenure", "NumOfProducts", "EstimatedSalary"]

scaler = MinMaxScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

X = df.drop("Exited", axis=True)
y = df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.20)

print(X_train.shape)

model = keras.Sequential(
    keras.layers.Dense(12, input_shape=(12,), activation="relu"),
    keras.layers.Dense(6, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid"),
)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# model.fit(X_train, y_train, epochs=20)
