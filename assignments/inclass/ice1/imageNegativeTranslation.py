import cv2

#----------Convert Gray image to Negative----------------
#g(x,y) = (L-1) - f(x,y)

#read image 
bitmap = cv2.imread("grayscale.jpeg", cv2.IMREAD_GRAYSCALE)
print(bitmap)
#define constant 
L = (2**8)
# create copy of np array to manipulate
neg_bitmap = bitmap.copy()

#apply equation to each element in bitmap
neg_bitmap = (L-1) - neg_bitmap

#print neg bitmap 
print(bitmap)

#show comparison of images 
cv2.imshow('Original Image', bitmap)
cv2.imshow('Negative Image',neg_bitmap)
cv2.waitKey(0)
cv2.destroyAllWindows()

