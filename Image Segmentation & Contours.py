# Image Segmatation using Contours
# Segmentation: Partitioning images into different regions
# Contours: Lines or curves around the boundary of an object

import cv2
# Import Numerical Python package - numpy as np
import numpy as np
# Read the image using imread built-in function
image = cv2.imread('C:/Users/NITESH/Downloads/Messi 2.jpg')
# Display original image using imshow built-in function
cv2.imshow("Original", image)
# Wait until any key is pressed
cv2.waitKey(0)
# cv2.Canny is the built-in function used to detect edges
# cv2.Canny(image, threshold_1, threshold_2)
canny = cv2.Canny(image, 50, 200)
# Display edge detected output image using imshow built-in function
cv2.imshow("Canny Edge Detection", canny)
# Wait until any key is pressed
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (255,255,255), 10)

cv2.imshow("Contours", image)
cv2.waitKey()
# Close all windows
cv2.destroyAllWindows()
