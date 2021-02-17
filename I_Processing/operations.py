from cv2 import cv2 
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('G:\\Python\\I_Processing\\eiffel.jpg',cv2.IMREAD_COLOR)
img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
img[100,100]=[255,255,255]
px=img[100,100]
# img[100:150,100:150]=[255,255,255]
watch_face=img[37:100,165:225]
img[0:63,0:60]=watch_face
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(px)