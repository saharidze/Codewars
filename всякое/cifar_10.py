from __future__ import annotations

import tensorflow as tf
from tensorflow.keras import datasets
from tensorflow.keras import layers
from tensorflow.keras import models

(train_images, train_labels), (
    test_images,
    test_labels,
) = datasets.cifar10.load_data()

train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()

model.add(
    layers.Conv2D(
        32, (3, 3), activation='relu',
        padding='same', input_shape=(32, 32, 3),
    ),
)
model.add(layers.BatchNormalization())
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.3))

model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.4))

model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10))

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metrics = ['accuracy']

# Компиляция модели
model.compile(
    optimizer=optimizer,
    loss=loss_fn,
    metrics=metrics,
)

history = model.fit(
    train_images, train_labels, epochs=10,
    validation_data=(test_images, test_labels),
)

accuracy = history.history['val_accuracy'][-1]

model_name = f'my_model_accuracy_{accuracy:.4f}.h5'
model.save(model_name)

# Оптимизация модели с помощью конвертации в TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

tflite_model_name = f'my_model_accuracy_{accuracy:.4f}.tflite'
with open(tflite_model_name, 'wb') as f:
    f.write(tflite_model)
