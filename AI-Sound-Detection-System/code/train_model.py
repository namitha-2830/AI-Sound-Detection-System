import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load extracted features
X = np.load("X.npy")  # shape (num_samples, num_features)
y = np.load("y.npy")  # shape (num_samples,)

# Convert labels to one-hot
y = tf.keras.utils.to_categorical(y)

# Build a simple model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(X, y, epochs=50, batch_size=16, validation_split=0.2)

# Save model (H5 format for compatibility)
model.save("saved_model/my_model.h5")