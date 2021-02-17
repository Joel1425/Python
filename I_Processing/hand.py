from cv2 import cv2
import numpy as np
cap=cv2.VideoCapture('G:\\Python\\I_Processing\\hand12.mp4')
human_cascade=cv2.CascadeClassifier('hand.xml')
while True:
    cord=[]
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
    human=human_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in human:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,220),3)
        cord.append([x,y,w,h])    
        cv2.imshow('video',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
print(cord)
cap.release()
cv2.destroyAllWindows()

