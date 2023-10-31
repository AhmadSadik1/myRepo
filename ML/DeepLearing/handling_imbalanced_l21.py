from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from tensorflow import keras
import tensorflow as tf
import pandas as pd

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = df.drop("customerID", axis="columns")

#! #################################################################################################!
# df1.gender.unique()
# df.Churn.value_counts():
# No     5174
# Yes    1869
# inputs.columns[inputs.isna().any()] search if there any null val 
# df.groupby('Category').describe()
#! #################################################################################################!


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

# model = keras.Sequential(
#     keras.layers.Dense(26, input_shape=(26,), activation="relu"),
#     keras.layers.Dense(15, activation="relu"),
#     keras.layers.Dense(1, activation="sigmoid"),
# )

# import tensorflow as tf
# from tensorflow import keras


# model = keras.Sequential([
#     keras.layers.Dense(26, input_shape=(26,), activation='relu'),
#     keras.layers.Dense(15, activation='relu'),
#     keras.layers.Dense(1, activation='sigmoid')
# ])

# opt = keras.optimizers.Adam(learning_rate=0.01)

# model.compile(optimizer='adam',
#               loss='binary_crossentropy',
#               metrics=['accuracy'])

# model.fit(X_train, y_train, epochs=100)

# model.evaluate(X_test, y_test)

# * under sampling : 
count_class_0 , count_class_1 = df.Churn.value_counts()

df_class_0 = df[df["Churn"] == 0]
df_class_1 = df[df["Churn"] == 1]

df_class_0_under = df_class_0.sample(count_class_1)
df_test_under = pd.concat([df_class_0_under,df_class_1], axis=0)

# ? over sampling
df_class_1_over = df_class_1.sample(count_class_0, replace=True)
df_test_over = pd.concat([df_class_0 , df_class_1_over], axis=0)

# ? SMOTE


smote = SMOTE(sampling_strategy='minority')
X_sm, y_sm = smote.fit_sample(X, y)

# ? Ensemble

def get_train_batch(df_majority, df_minority, start, end):
    df_train = pd.concat([df_majority[start:end], df_minority], axis=0)

    X_train = df_train.drop('Churn', axis='columns')
    y_train = df_train.Churn
    return X_train, y_train    