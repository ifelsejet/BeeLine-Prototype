import cv2
import numpy as np

filename = cv2.VideoCapture(1)

while(True):
    ret, frame = filename.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',frame)
    if cv2.waitKey(0) & 0xff == 27:
        break

filename.release()
cv2.destroyAllWindows()
