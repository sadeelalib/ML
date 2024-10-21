import cv2
import numpy as np

# Read the image from file
image = cv2.imread(r'C:\Users\PMLS\Desktop\Presentation\Machine Learning\OpenCV\techvista\sun.jpeg')
resized_image = cv2.resize(image, (300, 300))  # Resize to 400x300 pixels
v=np.hstack((resized_image,resized_image,resized_image))
h=np.vstack((v,v))

# Display the image in a window
cv2.imshow('YouExcel', v)
cv2.imshow('YouExcel', h)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()


