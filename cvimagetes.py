import cv2
import numpy as np
import matplotlib.pyplot as plt

#                                   0
img = cv2.imread(r"C:\Users\293746\Downloads\stawberry.png", cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1 
#IMREAD_UNCHANGED  = -1

#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#cv2.imshow('cv2.WINDOW_NORMAL', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [0,100], 'c', linewidth=5)
plt.show()
