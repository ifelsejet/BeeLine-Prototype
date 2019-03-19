import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:\\Users\\293746\\Downloads\\leomessi.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) #to hide tick values on X/Y vals
plt.show()
