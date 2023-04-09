#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)

# with mp_holistic.Holistic(min)
drawing = mp.solutions.drawing_utils
holistic = mp.solutions.holistic
h = holistic.Holistic(min_tracking_confidence=0.6, min_detection_confidence=0.6)
while True:
  ret, frame = cap.read()
  image = cv2.cvtColor(cv2.flip(frame , 1),cv2.COLOR_BGR2RGB)
  results = h.process(image)
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  # print(results.pose_landmarks)
  drawing.draw_landmarks(image, results.face_landmarks,holistic.FACEMESH_CONTOURS)
  drawing.draw_landmarks(image, results.left_hand_landmarks, holistic.HAND_CONNECTIONS)
  drawing.draw_landmarks(image, results.right_hand_landmarks, holistic.HAND_CONNECTIONS)
  drawing.draw_landmarks(image, results.pose_landmarks, holistic.POSE_CONNECTIONS,connection_drawing_spec=           drawing.DrawingSpec(color=(0, 255, 255),circle_radius=1,thickness=5))

  cv2.imshow("Hand Tracking",image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




