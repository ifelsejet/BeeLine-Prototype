# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import cv2 as cv
import numpy as np  
  
cap = cv.VideoCapture(1)  
  
# This drives the program into an infinite loop. 
while(1):        
    # Captures the live stream frame-by-frame 
    _, frame = cap.read()  
    # Converts images from BGR to HSV 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
    lower_red = np.array([110,50,50]) 
    upper_red = np.array([130,255,255]) 
  
# Here we are defining range of bluecolor in HSV 
# This creates a mask of blue coloured  
# objects found in the frame. 
mask = cv.inRange(hsv, lower_red, upper_red) 
  
# The bitwise and of the frame and mask is done so  
# that only the blue coloured objects are highlighted  
# and stored in res 
res = cv.bitwise_and(frame,frame, mask= mask) 
cv2.imshow('frame',frame) 
cv2.imshow('mask',mask) 
cv2.imshow('res',res) 
  
# This displays the frame, mask  
# and res which we created in 3 separate windows.

#k = cv2.waitKey(5) & 0xFF
#if k == 27: 
#break
  
# Destroys all of the HighGUI windows. 
cv.destroyAllWindows() 
  
# release the captured frame 
cap.release() 
