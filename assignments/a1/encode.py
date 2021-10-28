import numpy as np
import cv2

#create a 9 by 9 matrix
bitmap = np.array([[0,3,2,5,4,7,8,9,8], 
          [3,0,1,2,3,4,5,6,7],
          [2,1,0,3,2,5,4,7,6],
          [5,2,3,0,1,2,3,4,5],
          [4,3,2,1,0,3,2,5,4],
          [7,4,5,2,3,0,1,2,3],
          [6,5,4,3,2,1,0,3,2],
          [9,6,7,4,5,2,3,0,1],
          [9,7,6,5,4,3,2,1,0] 
          ])

#output to console original bitmap with size 
print("\t\t\t ORIGINAL BITMAP with size: " + str(bitmap.shape))
print(bitmap)

#pad bitmap
padded_bitmap = np.pad(bitmap,1,mode='constant', constant_values=0)

#duplicate original bitmap for new encoded vals
encoded_bitmap = bitmap.copy()

#-----------------------encode algorithm------------------------------------

#determine size of rows
row_size, col_size = bitmap.shape

#iterate through padded bitmap
for i in range(1,row_size+1):
    
    for j in range(1,col_size+1):

        #store element of interest 
        e = padded_bitmap[i][j]

        #store a temp list of neighbors
        topleft = padded_bitmap[i-1][j-1]
        topmid = padded_bitmap[i-1][j]
        topright = padded_bitmap[i-1][j+1]
        midleft = padded_bitmap[i][j-1]
        midright = padded_bitmap[i][j+1]
        lowleft = padded_bitmap[i+1][j-1]
        lowmid = padded_bitmap[i+1][j]
        lowright = padded_bitmap[i+1][j+1]

        #assign in symbol table counter clkwise
        neighbors = [topleft, midleft, lowleft, 
                    lowmid, lowright, midright, topright, topmid]

        #print("\t\t\t\te:" + str(e) + " type: " + str(type(e)))
        #print("all neighbors:")
        #print(neighbors)
#-----------------------------------------------------------------------
    #assign difference values
        for n in range(len(neighbors)):
            #difference is 0 or positive 
            if neighbors[n] >= e :
                #print(str(neighbors[n]) + ">=" + str(e))
                neighbors[n] = 1
            else :
            #difference is negative 
                #print(str(neighbors[n]) + "<" + str(e))
                neighbors[n] = 0
#-----------------------------------------------------------------------
        #print("difference:")
        #print(neighbors)
        #reverse list for big endian order 
        neighbors.reverse()
        #print("big endian: ")
        #print(neighbors)
        sum = 0

        #convert big endian into decimal 
        for indx in range(len(neighbors)):
            #print(str(sum)+" + 2^"+ str(indx)+ " *"+str(neighbors[indx]))
            sum = sum + (2**indx * neighbors[indx])

        #print("sum:" + str(sum))
        encoded_bitmap[i-1][j-1] = sum
#ouput to console encoded bitmap
print("\t\t\t ENCODED BITMAP with size: " + str(encoded_bitmap.shape))
print(encoded_bitmap)
