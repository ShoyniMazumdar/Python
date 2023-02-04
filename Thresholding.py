import cv2
image=cv2.imread("C:/Users/Nitesh/Downloads/girlwithapearlearring.jpg")
cv2.waitKey(0)

gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

thres_frame= cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]
thres_frame1= cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)[1]
thres_frame2= cv2.threshold(gray, 100, 255, cv2.THRESH_TRUNC)[1]
thres_frame3= cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO)[1]
thres_frame4= cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO_INV)[1]

cv2.imshow("Binary Frame", thres_frame)
cv2.imshow("Binary Inverse Frame", thres_frame1)
cv2.imshow("Trunk", thres_frame2)
cv2.imshow("To Zero", thres_frame3)
cv2.imshow("To Zero Inversed", thres_frame4)


cv2.waitKey(0)
cv2.destroyAllWindows()
