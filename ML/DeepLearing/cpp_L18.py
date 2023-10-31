from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import tensorflow as tf
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = df.drop("customerID", axis="columns")

# df1.gender.unique()


def print_object(df):
    for column in df:
        if df[column].dtype == "object":
            print(f"{column} : {df[column].unique()}")


def print_val(df):
    for col in df:
        print(f"{col}: {df[col].unique()}")


df["gender"].replace({"Female": 1, "Male": 0}, inplace=True)

df.replace("No internet service", "No", inplace=True)
df.replace("No phone service", "No", inplace=True)

yes_no_columns = [
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "PaperlessBilling",
    "Churn",
]

for col in yes_no_columns:
    df[col].replace({"Yes": 1, "No": 0}, inplace=True)

df = pd.get_dummies(data=df, columns=["InternetService", "Contract", "PaymentMethod"])

df = df[df["TotalCharges"] != " "]
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])

# print(df.columns)
# print_object(df)
# print_val(df)
# print(df.dtypes)


cols_to_scale = ["tenure", "MonthlyCharges", "TotalCharges"]

scaler = MinMaxScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

X = df.drop("Churn", axis="columns")
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

model = keras.Sequential(
    keras.layers.Dense(26, input_shape=(26,), activation="relu"),
    keras.layers.Dense(15, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid"),
)

import tensorflow as tf
from tensorflow import keras


model = keras.Sequential([
    keras.layers.Dense(26, input_shape=(26,), activation='relu'),
    keras.layers.Dense(15, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# opt = keras.optimizers.Adam(learning_rate=0.01)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100)

model.evaluate(X_test, y_test)
