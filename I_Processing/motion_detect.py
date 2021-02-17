from cv2 import cv2
import numpy as np
cap=cv2.VideoCapture('G:\\Python\\I_Processing\\footage.mp4')
human_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
while True:
    cord=[]
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    human=human_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in human:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,220),3)
        cord.append([x,y,w,h])    
        cv2.imshow('video',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
print(cord)
cap.release()
cv2.destroyAllWindows()

