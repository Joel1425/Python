from cv2 import cv2 
import numpy as np
import matplotlib.pyplot as plt
img1=cv2.imread('G:\\Python\\I_Processing\\taj.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('G:\\Python\\I_Processing\\black.jpg',cv2.IMREAD_COLOR)
# sub=img2-img1
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('Image',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(px)