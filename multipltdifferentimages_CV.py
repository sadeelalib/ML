import cv2
import numpy as np
import os

list_name = os.listdir(r"C:\Users\PMLS\Desktop\Presentation\Machine Learning\OpenCV\techvista")
print(list_name)

for name in list_name:
    path = (r"C:\\Users\\PMLS\\Desktop\\Presentation\\Machine Learning\\OpenCV\\techvista")
    img_name=path + "\\" + name
    img = cv2.imread(img_name)
    img = cv2.resize(img, (480, 480))
    cv2.imshow("Youexcel", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()