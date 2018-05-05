
import numpy as np
import cv2

#Define the video capture device or file
cap = cv2.VideoCapture(0)

facenoglass_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
facewithglass_cas = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()

    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect points
    facesnoglass = facenoglass_cas.detectMultiScale(gray, 1.3, 5)
    
    #draw detection rectangle
    for (x, y, w, h) in facesnoglass:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_colour = frame[y:y+h, x:x+w]
    
    #Display the resulting frame
    cv2.imshow('frame',frame)
    
    
    #Exit Condition
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        break

#Exit on complete
exit()
