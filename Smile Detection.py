# In this program we will detect Smile in a human Face

import cv2
import os
path = os.path.dirname(os.path.abspath(__file__))
print(path)
face_detect = cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml".format(path))
Smile_detect = cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_smile.xml".format(path))
capturing = cv2.imread("C:/Users/NITESH/Downloads/Selena.jpg")
resize_frame = cv2.resize(capturing, None, fx=0.2, fy=0.2,interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
face_detection = face_detect.detectMultiScale(gray, 1.3, 10)
for (x,y,w,h) in face_detection:
    gray_roi = gray[y:y+h, x:x+w]
    color_roi = resize_frame[y:y+h, x:x+w]
    Smily_detector = Smile_detect.detectMultiScale(gray_roi, 1.3, 5)
    for (smile_x, smile_y, smile_w, smile_h) in Smily_detector:
        cv2.rectangle(color_roi, (smile_x, smile_y), (smile_x + smile_w, smile_y + smile_h),
                                      (100,0,25), 5)
        cv2.imshow("Facial Emotion", resize_frame)
cv2.waitKey()
cv2.destroyAllWindows()
