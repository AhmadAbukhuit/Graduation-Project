import os
import random
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras import layers, models, optimizers

# Set random seed for reproducibility
seed = 42
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

# Set the path to your dataset
dataset_path = "/home/darkstorm/Desktop/TestDataset"
csv_path = "/home/darkstorm/Desktop/dataset.csv"

# Read CSV file
data_df = pd.read_csv(csv_path)

# Define parameters
img_size = (256, 256)  # Adjusted size
batch_size = 32
epochs = 10
num_classes = 11  # 10 types of malware + non-malware class

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

# Use the CSV data to create train and validation data generators
train_generator = train_datagen.flow_from_dataframe(
    dataframe=data_df,
    directory=dataset_path,
    x_col="Image_Path",  # Replace with the correct column name
    y_col="Class_Label",      # Replace with the correct column name
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_dataframe(
    dataframe=data_df,
    directory=dataset_path,
    x_col="Image_Path",  # Replace with the correct column name
    y_col="Class_Label",      # Replace with the correct column name
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Load the pre-trained InceptionV3 model
base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(256, 256, 3))

# Freeze the layers of the pre-trained model
base_model.trainable = False

# Create a custom model on top of the pre-trained model
model = models.Sequential()
model.add(base_model)
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size
)

# Save the model
model.save("malware_classification_model.keras")

# Evaluate the model
loss, accuracy = model.evaluate(validation_generator)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

