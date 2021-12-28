import cv2
import numpy as np
import dlib

#(0) in VideoCapture is used to
# connect to your compute's defaut camera
cap = cv2.VideoCapture(0)

#get the coordinates
detector = dlib.get_frontal_face_detector()

while True:
  #capture frame-by-frame
  ret, frame = cap.read()
  frame = cv2.flip(frame,1)

  #our operation on the frame come hereq
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces = detector(gray)
  # counter to count number of faces
  i=0

  for face in faces:
    x, y = face.left(), face.top()
    x1, y1 = face.right(), face.bottom()
    cv2.rectangle(frame, (x,y),(x1,y1),(0,255,0),2)

    # incrment the iterator each time you get the coordinates
    i=i+1

    #adding face number to the box dectecting faces
    cv2.putText(frame, 'face num' + str(i),(x-10,y-10),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    print(face,i)

  # Display the resulting frame
  cv2.imshow('frame', frame)

  #Enter key "q" to break the loop
  if cv2.waitKey(1)& 0xFF == ord('q'):
    break


# when everthing done , release
# the capture and destroy the windows

cap.release()
cv2.destroyAllWindows()