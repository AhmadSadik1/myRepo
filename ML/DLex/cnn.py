# %%
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import tensorflow as tf
import pandas as pd

(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()
(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()
X_train.shape
# (60000, 28, 28)
X_test.shape
# (10000, 28, 28)
X_train[0].shape
# (28, 28)
X_train = X_train / 255
X_test = X_test / 255

X_test = X_test.reshape(-1,28,28,1)
X_test.shape

model = keras.Sequential([
    keras.layers.Conv2D(30, (3,3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2,2)),
 
    keras.layers.Flatten(),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5)
model.evaluate(X_test,y_test)