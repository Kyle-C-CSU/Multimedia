#Binary Image Transformation 
#g(x,y) = { 0,  f(x,y)<t
#          L-1, f(x,y)>=t
#                        }
#L = 2**8   t = 40,80,120,...

#include OpenCV
import cv2
import numpy as np
import sys

#get path and image
image = 'dog.jpeg'
#read bitmap from image
bitmap = cv2.imread(image,cv2.IMREAD_GRAYSCALE)

# create copy of np array to manipulate
mul_bitmap = bitmap.copy()
# create copy of np array to manipulate
div_bitmap = bitmap.copy()
# create copy of np array to manipulate
bt_bitmap = bitmap.copy()
# create copy of np array to manipulate
comp_bitmap = bitmap.copy()

#define Constants L = max color value, t = thresh hold  
L, t = 2**8, 80

#1 multiply by 2
mul_bitmap = bitmap * 2
#2 div by 2
div_bitmap = bitmap / 2
#3 binary transition
#uint8 unsigned int 8 (grayscale)
#lambda needs to understand uint for # of channels 
bt_bitmap = np.uint8(list(map(lambda x:  list(0 if i < t else L-1 for i in x), bitmap)))
#4 complement of binary transition
comp_bitmap = 255 - bt_bitmap

#display final image
cv2.imshow('Original Image', bitmap) 
cv2.imshow('Mult by 2' ,mul_bitmap)
cv2.imshow('Div by 2', div_bitmap)
cv2.imshow('Binary Transition', bt_bitmap)
cv2.imshow('Complement of Binary Transition', comp_bitmap)
cv2.waitKey(0)