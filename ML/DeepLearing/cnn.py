# %%
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

# print(X_train.shape)
# print(X_test.shape)

# print(y_train[0])
# print(X_train[0])

y_train = y_train.reshape(-1)
y_test = y_test.reshape(-1)

classes = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def plot_sample(X, y, index):
    plt.figure(figsize=(15, 2))
    plt.imshow(X[index])
    plt.xlabel(classes[y[index]])


plot_sample(X_train, y_train, 1)


X_train = X_train / 255.0
y_train = y_train / 255.0

cnn = (
    models.Sequential(
        [
            layers.Conv2D(
                filters=32,
                kernel_size=(3, 3),
                activation="relu",
                input_shape=(32, 32, 3),
            ),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPool2D((2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(32, activation="softmax"),
        ]
    ),
)
cnn.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)
cnn.fit(X_train, y_train, epochs=10)
cnn.evaluate(X_test, y_test)

# %%


cnn = keras.Sequential(
    [
        layers.Conv2D(
            filters=32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28)
        ),
        layers.MaxPool2D((2, 2)),
        layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPool2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(64, activation="relu"),
        layers.Dense(32, activation="softmax"),
    ]
)
cnn.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)
cnn.fit(X_train, y_train, epochs=10)

