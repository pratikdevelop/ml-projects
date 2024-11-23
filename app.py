import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from keras import datasets

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

# Normalize the image data to range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Class names for CIFAR-10 dataset
classNames = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Optional: Upscale images for clarity using cv2
x_train_upscaled = np.array([
    cv.resize(img, (60, 60), interpolation=cv.INTER_CUBIC) for img in x_train[:16]
])

# Plotting 16 images with labels
plt.figure(figsize=(10, 10), dpi=150)  # Increase DPI for sharpness
for i in range(16):
    plt.subplot(4, 4, i + 1)
    plt.yticks([])
    plt.xticks([])
    
    # Display the upscaled image
    plt.imshow(x_train_upscaled[i], interpolation='none')  # No additional smoothing
    plt.xlabel(classNames[y_train[i][0]], fontsize=10)  # Add label with larger font size

# Display the plot
plt.tight_layout()
plt.show()
