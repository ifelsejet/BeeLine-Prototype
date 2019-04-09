import cv2 
import numpy as np
input_image = cv2.imread(r"C:\Users\293746\Downloads\opencvlogo.png", cv2.IMREAD_COLOR)
# set kernel as 3x3 matrix from numpy
kernel = np.ones((3,3), np.uint8)
#Create erosion and dilation image from the original image
erosion_image = cv2.erode(input_image, kernel, iterations=1)
dilation_image = cv2.dilate(input_image, kernel, iterations=1)
cv2.imshow('Input', input_image)
cv2.imshow('Erosion', erosion_image)
cv2.imshow('Dilation', dilation_image)
#wait for a key to exit
cv2.waitKey(0)      
