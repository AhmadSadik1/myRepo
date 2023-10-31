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


class myNN:
    def __init__(self):
        self.w1 = 1
        self.w2 = 1
        self.bias = 0

    def fit(self, X, y, epochs, loss_thresold):
        self.w1, self.w2, self.bias = self.gradient_descent(X["age"] , X["affordibility"], y , epochs , loss_thresold)
    
    def predict(self , X_test):
        weighted_sum = self.w1*X_test['age'] + self.w2*X_test['affordibility'] + self.bias
        return sigmoid_numpy(weighted_sum)

    def gradient_descent(self, age, affordibllity, y_true, epochs, loss_thresold):
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

            if i%50==0:
                print (f'Epoch:{i}, w1:{w1}, w2:{w2}, bias:{bias}, loss:{loss}')
            

            if loss <= loss_thresold:
                break

        return w1, w2, bias


customModel = myNN()
customModel.fit(X_train_S, y_train, epochs=8000, loss_thresold=0.4631)