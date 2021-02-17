from cv2 import cv2 
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('G:\\Python\\I_Processing\\eiffel.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()
cv2.imwrite('eiffelgray.jpg',img)
# cv2.imshow('Eiffel',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
