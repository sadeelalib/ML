import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Generate dummy data
X_train = np.random.rand(1000, 20)  # 1000 samples, 20 features
y_train = np.random.randint(2, size=(1000, 1))  # Binary classification

print(X_train[:5])
print(y_train[:5])

'''
# Create MLP model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(20,)),  # Input layer + hidden layer
    layers.Dense(32, activation='relu'),  # Hidden layer
    layers.Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)
'''