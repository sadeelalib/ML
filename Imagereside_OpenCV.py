import cv2

# Read the image from file
image = cv2.imread(r'C:\Users\PMLS\Desktop\Presentation\Machine Learning\OpenCV\techvista\sun.jpeg')
resized_image = cv2.resize(image, (400, 200))  # Resize to 400x300 pixels
# Display the image in a window
cv2.imshow('Image Window', resized_image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()


