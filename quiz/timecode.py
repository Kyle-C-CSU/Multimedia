import cv2

videoIn = cv2.VideoCapture("basketball.avi")

videoOut = cv2.VideoWriter("basketballModified.avi", 0x7634706d, 30, (400,300))

success, image1 = videoIn.read()
while success:
    image2 = cv2.resize(image1, (400, 300))
    videoOut.write(image2)
    success, image1 = videoIn.read()

videoIn.release()
videoOut.release() 
