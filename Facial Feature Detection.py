import cv2

face_detect=cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
Nose_detect=cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_nose.xml")
Eye_detect=cv2.CascadeClassifier("C:/Users/NITESH/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_eye.xml")

cap=cv2.VideoCapture(0)



while 1:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.3,5)
    
    for (x,y,h,w) in face_detection:
        gray_roi=gray[y:y+h, x:x+w]
        color_roi=img[y:y+h, x:x+w]

        nose_detector = Nose_detect.detectMultiScale(gray_roi, 1.3, 5)
        for (nose_x, nose_y, nose_w, nose_h) in nose_detector:
            cv2.rectangle(color_roi, (nose_x, nose_y), (nose_x + nose_w, nose_y + nose_h),(100,0,25), 5)

        eye_detector = Eye_detect.detectMultiScale(gray_roi,1.3,5)
        for (eye_x, eye_y, eye_w, eye_h) in eye_detector:
            cv2.rectangle(color_roi,(eye_x,eye_y),(eye_x + eye_w, eye_y + eye_h),(100,0,25),5)

    cv2.imshow("Facial Feature Detection",img)
    Key=cv2.waitKey(0)& 0xff
    if (Key==27):
        break
    
cap.release()
#This is to release camera
cv2.waitKey()
cv2.destroyAllWindows()
#This is to destroy the openwindow
