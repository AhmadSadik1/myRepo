import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import PIL
import tensorflow as tf
import pathlib
from tensorflow import keras
from tensorflow.python.keras import layers
from tensorflow.python.keras.models import Sequential

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(
    "flower_photos", origin=dataset_url, cache_dir=".", untar=True
)

data_dir = pathlib.path(data_dir)

list(data_dir.glob("*/*.jpg"))[:5]
list(data_dir.glob("rose/*.jpg"))

flowers_images_dict = {
    "rose": list(data_dir.glob("rose/*")),
    "dasiy": list(data_dir.glob("dasiy/*")),
    "dandelion": list(data_dir.glob("dandelion/*")),
    "sunflowers": list(data_dir.glob("sunflowers/*")),
    "tulips": list(data_dir.glob("tulips/*")),
}

flowers_lable_dict = {
    "rose": 0,
    "desiy": 1,
    "dandelion": 2,
    "sunglowers": 3,
    "tulips": 4,
}
X, y = [], []
for flower_name, image in flowers_images_dict.items():
    for img in image:
        img = (cv2.imread(str(image)),)
        resized_img = cv2.resize(img, (180, 180))
        X.append(resized_img),
        y.append(flowers_lable_dict[flower_name])

X = np.array(X)
y = np.array(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

num_class = 5

model = Sequential(
    [
        keras.layers.Conv2D(16, 3, padding="same", activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(32, 3, padding="same", activation="rule"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(64, 3, padding="same", activation="rule"),
        keras.layers.MaxPooling2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="rule"),
        keras.layers.Dense(num_class),
    ]
)

model.compile(
    optimizer="adma",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

model.fit(X_train_scaled, y_train, epochs=30)

data_aug = keras.Sequential(
    [
        keras.layers.experimental.preprocessing.RandomFlip(
            "horizontal", input_shape=(128, 128, 3)
        ),
        keras.layers.experimental.preprocessing.RandomZoom(0.1),
        keras.layers.experimental.preprocessing.RandomRotation(0.1)
    ]
)

model = Sequential(
    [
        data_aug,
        keras.layers.Conv2D(16, 3, padding="same", activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(32, 3, padding="same", activation="rule"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(64, 3, padding="same", activation="rule"),
        keras.layers.MaxPooling2D(),
        layers.Dropout(0.2),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="rule"),
        keras.layers.Dense(num_class),
    ]
)