#g(x,y) = {0        if f(x,y) < t1
#          f(x,y)   if t1 < f(x,y) < t2
#          0        if t2 > f(x,y)
# t1 = 255/3    t2 = (255/3)+(255/3)
#}

#include OpenCV
import sys
import cv2
import numpy as np

#define path and image
path, image = 'images/', sys.argv[1]
#define thresholds
t1,t2 = (255/3), (255/3)+(255/3)
#read image from command line 
bitmap = cv2.imread(path+image,cv2.IMREAD_GRAYSCALE)
# create copy of np array to manipulate
ir_bitmap = bitmap.copy()
#apply map 
ir_bitmap = list(map(lambda bm: list(0 if pix < t1 or pix > t2 else pix for pix in bm),bitmap))
#convert mapobject into np unsigned int for cv2.imshow 
ir_bitmap = np.uint8(ir_bitmap)
#show Interval Reservation image
cv2.imshow('Original Image', bitmap)
cv2.imshow('Interval Reservation', ir_bitmap)
cv2.waitKey(0)
    
