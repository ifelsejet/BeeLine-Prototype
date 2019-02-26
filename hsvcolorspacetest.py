import cv2 as cv
import numpy as np
cap = cv.VideoCapture(1)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    #define range of green color in HSV
    lower_green = np.array([60,100, 100])
    upper_green = np.array([80, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    #Threshold the HSV image to get only green colors
    greenMask = cv.inRange(hsv,  lower_green, upper_green)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    #res2 = cv.bitwise_and(frame, frame, greenMask= greenMask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('greenMask', greenMask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
