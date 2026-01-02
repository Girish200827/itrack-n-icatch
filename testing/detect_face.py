import cv2 as cv
import numpy as np
import time as t

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +
'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Display fps
    
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    cv.imshow('Faces', faces)
    if cv.waitKey(1) == ord('p'):
        break
        
cap.release()
cv.destroyAllWindows()