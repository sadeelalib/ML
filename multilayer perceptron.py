# Required Libraries Import Karna
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# 1. Data Load Karna
# MNIST dataset ko load karna
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# 2. Data Preprocessing
# Tasveeron ko flatten karna (28x28 se 784 dimensional vector mein)
X_train = X_train.reshape((X_train.shape[0], 28 * 28)).astype('float32') / 255
X_test = X_test.reshape((X_test.shape[0], 28 * 28)).astype('float32') / 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# 3. Creating MLP Model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),  # First hidden layer
    layers.Dense(64, activation='relu'),                       # Second hidden layer
    layers.Dense(10, activation='softmax')                     # Output layer
])

# 4. Model Compilation
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 5. Model Training
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# 6. Model ki Evaluation
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_accuracy:.4f}')

# Kisi Tasveer ka Peshgoi Dikhana
sample_image = X_test[4].reshape(28, 28)
plt.imshow(sample_image, cmap='gray')
plt.title(f'Predicted: {np.argmax(model.predict(X_test[4].reshape(1, 784)))}')
plt.show()


actual_label = np.argmax(y_test[2])  # Yahan y_test[0] ko bhi check kar sakte hain
print(f'Actual Label: {actual_label}')
