# In this program we will detect Eyes of a image
import cv2
import os
path = os.path.dirname(os.path.abspath(__file__))
face_detect = cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
eyes_detect = cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye.xml")
capturing = cv2.imread("C:/Users/NITESH/Downloads/Selena.jpg")
resize_frame = cv2.resize(capturing, None, fx=1, fy=1,interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
face_detection = face_detect.detectMultiScale(gray, 1.3, 10)
for (x,y,w,h) in face_detection:
                gray_roi = gray[y:y+h, x:x+w]
                color_roi = resize_frame[y:y+h, x:x+w]
                eye_detector = eyes_detect.detectMultiScale(gray_roi,1.3,5)
                for (eye_x, eye_y, eye_w, eye_h) in eye_detector:
                        cv2.rectangle(color_roi,(eye_x,eye_y),(eye_x + eye_w, eye_y + eye_h),(255,0,0),5)
cv2.imshow("DetectFace", resize_frame)
cv2.waitKey()

cv2.destroyAllWindows()
