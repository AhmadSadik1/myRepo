import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# print(len(X_train))
# print(len(X_test))

# X_train[0]
# X_train.shape
# X_train[0].shape

# X_train_flattened = X_train.reshape(len(X_train), 28 * 28)
# X_test_flattened = X_test.reshape(len(X_test), 28 * 28)

# X_train_flattened.shape
# X_test_flattened.shape

# model = keras.Sequential(
#     [
#         keras.layers.Flatten(input_shape=(28, 28)),
#         keras.layers.Dense(100, activation="relu"),
#         keras.layers.Dense(10, activation="sigmoid"),
#     ]
# )

# model.compile(
#     optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
# )

# model.fit(X_train, y_train, epochs=10)
# model.evaluate(X_test, y_test)
