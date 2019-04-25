import cv2
import sys
import numpy as np

#Read image
image = cv2.imread("../assets/putin.jpg", cv2.IMREAD_GRAYSCALE)

#check if image exits
if image is None:
    print("can not find image")
    sys.exit()

#apply sobel filter along X direction
gradientX = cv2.Sobel(image, cv2.CV_32F, 1, 0)

#apply sobel filter along Y direction
gradientY = cv2.Sobel(image, cv2.CV_32F, 0, 1)

#normalize images to display
cv2.normalize(gradientX, dst=gradientX, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
cv2.normalize(gradientY, dst=gradientY, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

#create windows to display images
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagex", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagey", cv2.WINDOW_NORMAL)

#display images
cv2.imshow("image", image)
cv2.imshow("imagex", gradientX)
cv2.imshow("imagey", gradientY)

#press esc to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()