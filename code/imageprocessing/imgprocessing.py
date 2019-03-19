import numpy as np
import cv2 as cv

#Load an color image in grayscale
img = cv.imread('C:\\Users\\293746\\Downloads\\leomessi.jpg',0)
#Display new grayscale image
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()
