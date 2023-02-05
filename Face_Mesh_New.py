import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)
facemesh = mp.solutions.face_mesh
face = facemesh.FaceMesh(static_image_mode=True , min_tracking_confidence=0.6,min_detection_confidence=0.6)
draw=mp.solutions.drawing_utils

while True:
   ret, frame = cap.read()
   rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   output = face.process(rgb)
   # print(output.multi_face_landmarks)
   if output.multi_face_landmarks:
       for i in output.multi_face_landmarks:
           draw.draw_landmarks(frame ,i,facemesh.FACEMESH_CONTOURS,landmark_drawing_spec=draw.DrawingSpec(color=(255,0,255),circle_radius=1,thickness=1))
   cv2.imshow("Face Mesh Window",frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
