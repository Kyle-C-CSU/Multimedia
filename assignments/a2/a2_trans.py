"""
3. Write programs to perform the following transformations 
on the grayscale images (you may pick any image). Display 
the output images along with the respective input images. 

"""

import cv2
import numpy as np
import math 
#---------------------------------------------------------------------------
#                       Read Gray Scale Image 
#---------------------------------------------------------------------------
#get path and image
image = 'html/images/MrDams.png'
#read bitmap from image
bitmap = cv2.imread(image,cv2.IMREAD_GRAYSCALE)

#---------------------------------------------------------------------------
"""                     Binary Transformation 

g(x,y) = { 0,  f(x,y)<t
          L-1, f(x,y)>=t
                        }
L = max color value,    t = thresh hold
L = 2**8                t = 70 and 170
"""
#---------------------------------------------------------------------------
#define Constants   
L, t1, t2 = 2**8, 70, 170

# Create 2 copies of bitmap for 2 thresh holds 
t1_bitmap = bitmap.copy()
t2_bitmap = bitmap.copy()

#uint8 unsigned int 8 (grayscale)
#lambda needs to understand uint for # of channels 
t1_bitmap = np.uint8(list
                    (map(lambda x:  list
                    (0 if i < t1 else L-1 for i in x), bitmap)))
t2_bitmap = np.uint8(list
                    (map(lambda x:  list
                    (0 if i < t2 else L-1 for i in x), bitmap)))

#---------------------------------------------------------------------------
"""                     Interval Reservation 
g(x,y) = {0        if f(x,y) < t1
          f(x,y)   if t1 < f(x,y) < t2
          0        if t2 > f(x,y)
          }
where,  t1 = 70   t2 = 170
"""
#---------------------------------------------------------------------------
# Create copy of bitmap for comparison 
ir_bitmap = bitmap.copy()

#uint8 unsigned int 8 (grayscale)
#lambda needs to understand uint for # of channels 
ir_bitmap = np.uint8(list
                    (map(lambda bm: list
                    (0 if pix < t1 or pix > t2 else pix for pix in bm),bitmap)))

#---------------------------------------------------------------------------
"""                    Log base 10 Transformation 
S = C log(1+r)
where, C = 255/log(1+255) 
therefor, C = 105.88
"""
#---------------------------------------------------------------------------
#define constants 
C =105.88

# Create copy of bitmap for comparison 
log_bitmap = bitmap.copy()

#uint8 unsigned int 8 (grayscale)
#lambda needs to understand uint for # of channels 
log_bitmap = np.uint8(list(map(lambda bm: 
                      list(C*(math.log10(1+pix)) for pix in bm),bitmap)))

#---------------------------------------------------------------------------
"""                    Gamma Correction Transformation
S = C r ^ gamma  
where, C = 255/255**gamma
therefor,
"""
#---------------------------------------------------------------------------

#Gamma has three values g1 < 1 < g2
g1,g2 = .57, 1.57
C1,C2 = (255/(255)**g1), (255/(255)**g2)

#create copy of bitmap 
gamma_bitmap = bitmap.copy()

#map gamma values 
g1_bitmap = np.uint8(list(map(lambda bm: 
                     list((C1*(pix)**g1) for pix in bm),bitmap)))
                        
g2_bitmap = np.uint8(list(map(lambda bm:
                        list((C2*(pix)**g2)for pix in bm),bitmap)))

#---------------------------------------------------------------------------                 Display Images  
#                       Display Images 
#---------------------------------------------------------------------------

cv2.imshow('Original Image', bitmap) 
cv2.imshow('Binary Transformation Thresh hold 1' ,t1_bitmap)
cv2.imshow('Binary Transformation Thresh hold 2', t2_bitmap)
cv2.imshow('Iterval Reservation Transformation' ,ir_bitmap)
cv2.imshow('Log Base 10 Transformation', log_bitmap)
cv2.imshow('Gamma1 Correction Transformatoin' ,g1_bitmap)
cv2.imshow('Gamma2 Correction Transformation' ,g2_bitmap)
cv2.waitKey(0)