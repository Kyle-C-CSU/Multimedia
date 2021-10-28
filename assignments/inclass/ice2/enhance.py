import cv2
import numpy 

img = cv2.imread("fuji.png")
bitmap = img.copy()

R = 76.245
G = 149.685
B = 29.071
total = 0
row, col, _ = img.shape
for i in range(row):
    for j in range(col):
        b = img[i][j][0]*B
        g = img[i][j][1]*G
        r = img[i][j][2]*R
        bitmap[i][j]  = (r+b+g)/255


print(bitmap[0][0])
#cv2.waitKey(0)

