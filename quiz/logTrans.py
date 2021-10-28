#S = Clog(1+ r)
def calcS(r,C):
    return (C*(math.log10(1+r)))
      


#include OpenCV
import cv2
import numpy as np
import sys
#include log10
import math

#read path and image
path, image = 'images/', sys.argv[1]
bitmap = cv2.imread(path+image,cv2.IMREAD_GRAYSCALE)
# create copy of np array to manipulate
log_bitmap = bitmap.copy()
#define C = 255/log(1+255)
C = 105.88
#apply map 
log_bitmap = list(map(lambda bm: list(C*(math.log10(1+pix)) for pix in bm),bitmap))
#convert map object to uint
log_bitmap = np.uint8(log_bitmap)
#Show Log Base 10 Transformation image 
cv2.imshow('Original Image', bitmap)
cv2.imshow('Log Base 10 Transformation', log_bitmap)
cv2.waitKey(0)
    