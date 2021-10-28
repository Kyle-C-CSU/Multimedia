import cv2 
import copy

#Create Python program that implements Huffman coding technique to reduce the enclosed image 
#file size (not the image dimenssion).
#Save the output file and the key codes.
#Compare the image file size before and after. 

#------------------------------------------------------------------------------------------
#                                           Helper Functions
#------------------------------------------------------------------------------------------
#Sort Dictionary by values 
def sort_dict(dictionary):
    return {k: v for k, v in sorted(dictionary.items(),reverse=True, key=lambda item: item[1])}

#------------------------------------------------------------------------------------------
#                                           Read image 
#------------------------------------------------------------------------------------------
def readImg(path = "quiz2.png"):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    return img 

#------------------------------------------------------------------------------------------
#                                           Get Frequency
#------------------------------------------------------------------------------------------
def getFreq(img):
    #get row and col of gray scale 
    row,col = img.shape
    intensities = []
    freq = {}
    for i in range(row):
        for j in range(col):
            intensities.append(img[i][j])
    intensities.sort()
    for i in intensities:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    return freq
#------------------------------------------------------------------------------------------
#                                   Get Probability density 
#------------------------------------------------------------------------------------------
def getPrk(img,freq):
    m,n = img.shape
    MN = m*n
    prk = {}
    for i in freq:
        prk[i]=float(freq[i]/MN) 
    prk = sort_dict(prk)
    return prk

#------------------------------------------------------------------------------------------
#                                       Get Stages
'''
    Fix this to have tuples in the list that have the values
            stage, color, prk, bits
'''
#------------------------------------------------------------------------------------------
def getStages(prk):
    prob_dens = list(prk.values())
    size = len(prob_dens)
    stages = {}
    stages = copy.deepcopy(stages)
    stages[0] = prob_dens
    #maybe have instances of lists to save each iteration
    for i in range(1,size):
        # print('#------------------------------------------------------------------------------------------')
        if len(prob_dens)>2:
            #make deep copy so dictionary dosent have same reference for r
            stages = copy.deepcopy(stages)
            tail = prob_dens.pop() + prob_dens.pop() 
            prob_dens.append(tail)
            prob_dens.sort(reverse=True)
            stages[i]= prob_dens
    #         for j in range(0,4):
    #             if(j <=1):
    #                 print(j,end='')
    #                 print(':',r[j])
    #             if (j > 2):
    #                 print(' .','\n','.','\n','.','\n')
    #                 print(len(r)-2,':',r[len(r)-2])
    #                 print(len(r)-1,':',r[len(r)-1])

    
    # print(stages)
    return stages

#------------------------------------------------------------------------------------------
#                                       Assign bits 
'''
This will assign the smallest binary value to each color value in the stages
Must reuse the same binary value for the same color 
Edge case: could have same prk value but be different color must acount for that 
'''
#------------------------------------------------------------------------------------------
#might need to create a class for tuples to hold:
#   color, index, prk, bit/s


#checkColorAssigned(bits,color)
#assignPrevBit(bits,color)
#assignNewBit(bits, color)

# def getBits(stages):
#     #color: bit/s 
#     bits = {}

#     for keys in reversed(stages):
#         bits=copy.deepcopy(bits)
#         temp_bits = []
#         for i in stages[keys]:
#             if checkColorAssigned(bits,i):
#                 prev_bit = assignPrevBit(bits,i)
#                 temp_bits.append(prev_bit)   
#             else:
#                 new_bit = assignNewBit(bits,i)
#                 temp_bits.append()
#         bits[stages[key]]=temp_bits
        
#------------------------------------------------------------------------------------------
#                                        MAIN
#------------------------------------------------------------------------------------------
img = readImg()
freq = getFreq(img)
prk = getPrk(img,freq)
stages = getStages(prk)
print(stages)    

# cv2.imshow("original",img)
# cv2.waitKey(0)
