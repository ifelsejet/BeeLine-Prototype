import cv2

print(cv2.__file__)
print(cv2.__version__)

print("FFMPEG: ")
print(cv2.CAP_FFMPEG)
print("IMAGES: ")
print(cv2.CAP_IMAGES)
print("MSMF: ")
print(cv2.CAP_MSMF)
        # http://answers.opencv.org/question/34461/how-to-set-camera-resolution-webcam-with-opencv/
print("WIDTH prop ID: ")
print(cv2.CAP_PROP_FRAME_WIDTH)
print("HEIGHT prop ID: ")
print(cv2.CAP_PROP_FRAME_HEIGHT)

video = cv2.VideoCapture(0)
print (video.isOpened()) # False
print (video.read()) # (False, None)
