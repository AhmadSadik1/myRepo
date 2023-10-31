from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf
import pandas as pd
import numpy as np
import math

df = pd.read_csv(r"C:\Users\Ahmad\Desktop\exfile\gradient_descent_insurance_data.csv")

X = df.drop(["bought_insurance"], axis="columns")
y = df["bought_insurance"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train_S = X_train.copy()
X_train_S["age"] = X_train_S["age"] / 100

X_test_S = X_test.copy()
X_test_S["age"] = X_test_S["age"] / 100

model = keras.Sequential(
    keras.layers.Dense(
        1,
        input_shape=(2,),
        activation="sigmoid",
        kernel_initializer="ones",
        bias_initializer="zeros",
    )
)

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train_S, y_train, epochs=5000)

# print(model.evaluate(X_test_S,y_test))

# print(model.predict(X_test_S))

conf, ints = model.get_weights()
# print(conf)
# print(ints)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def prediction_function(age, affordibility):
    weights_sum = conf[0] * age + conf[1] * affordibility + ints
    return sigmoid(prediction_function)


# print(prediction_function(.47, 1))


def sigmoid_numpy(X):
    return 1 / (1 + np.exp(-X))


def log_loss(y_true, y_predicted):
    epsilon = 1e-15
    y_predicted_new = [max(i, epsilon) for i in y_predicted]
    y_predicted_new = [min(i, 1 - epsilon) for i in y_predicted_new]
    y_predicted_new = np.array(y_predicted_new)
    return -np.mean(
        y_true * np.log(y_predicted_new) + (1 - y_true) * np.log(1 - y_predicted_new)
    )


def gradient_descent(age, affordibllity, y_true, epochs, loss_thresold):
    w1 = w2 = 1
    bias = 1
    rate = 0.5
    n = len(age)

    for i in range(epochs):
        weights_sum = w1 * age + w2 * affordibllity + bias
        y_predicted = sigmoid_numpy(weights_sum)
        loss = log_loss(y_true, y_predicted)

        w1d = (1 / n) * np.dot(np.transpose(age), (y_predicted - y_true))
        w2d = (1 / n) * np.dot(np.transpose(affordibllity), (y_predicted - y_true))

        bias_d = np.mean(y_predicted - y_true)
        w1 = w1 - rate * w1d
        w2 = w2 - rate * w2d

        print(f"Epoch:{i}, w1:{w1}, w2:{w2}, bias:{bias}, loss:{loss}")

        if loss <= loss_thresold:
            break

    return w1, w2, bias


gradient_descent(X_train_S["age"], X_train_S["affordibility"], y_train, 1000, 0.4631)
