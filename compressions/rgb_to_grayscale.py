import cv2

parrot = cv2.imread('parrot.jpeg')
imggray = cv2.imread('parrot.jpeg',0)
#cv2.imshow('gray image',imggray)
cv2.imshow('parrot', parrot)
cv2.waitkey(0)
cv2.destroyallwindows() 

