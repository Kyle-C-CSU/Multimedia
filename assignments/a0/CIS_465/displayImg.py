import cv2
#read an image
img = cv2.imread('images/kingJames.jpg')
#displa an image
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
