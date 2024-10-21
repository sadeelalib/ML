import cv2

# Read the image from file
image = cv2.imread(r'C:\Users\PMLS\Desktop\Presentation\Machine Learning\OpenCV\banner.jpg')

# Display the image in a window
cv2.imshow('YouExcel', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
