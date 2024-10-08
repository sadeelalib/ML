import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

# MNIST dataset load karna
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Pehli 5 images aur labels ko print karna
for i in range(20):
    # Image ko print karna
    plt.imshow(X_train[i], cmap='gray')  # Grayscale mein display karna
    plt.title(f"Label: {y_train[i]}")
    plt.show()

# Pehli image ke raw pixel values ko print karna
print("Pehli image ke pixel values:")
print(X_train[0])

# Pehli image ka label
print(f"Pehli image ka label: {y_train[0]}")



'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load image from the path
image_path = "C:/Users/PMLS/downloads/7.jpeg"
image = Image.open(image_path)

# Step 2: Convert image to grayscale
image = image.convert('L')  # 'L' mode converts it to grayscale

# Step 3: Resize the image to 28x28 pixels
image = image.resize((28, 28))

# Step 4: Normalize pixel values (0 to 1)
image_array = np.array(image) / 255.0

# Step 5: Display the processed image
plt.imshow(image_array, cmap='gray')
plt.title("Processed Image (28x28)")
plt.show()

# Step 6: Print the image array (pixel values)
print(image_array)
'''