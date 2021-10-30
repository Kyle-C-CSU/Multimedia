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

#Sort Tuple by 2nd value 
def Sort_Tuple(tup): 
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    # sublist lambda has been used 
    tup.sort(key = lambda x: x[1],reverse=True) 
    return tup 
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
def corcoranStage(prk):
    corcoranS = []
    for i in prk:
        corcoranS.append((i,prk[i]))
    return corcoranS

#------------------------------------------------------------------------------------------
#                                       Assign bits 
'''
This will assign the smallest binary value to each color value in the stages
Must reuse the same binary value for the same color 
Edge case: could have same prk value but be different color must acount for that 
'''
#------------------------------------------------------------------------------------------
def lowestBitDepthVal(used_bits):
    for i in range(255):
        if bin(i)[2:] not in used_bits:
            return bin(i)[2:]
    #error 
    return -1

def getBits(stages):
    used_bits = []
    bits = []
    for element in stages:
        new_bit = lowestBitDepthVal(used_bits)
        used_bits.append(new_bit)
        bits.append((element[0],element[1],new_bit))    
    return bits
#------------------------------------------------------------------------------------------
#                                        MAP
#------------------------------------------------------------------------------------------
def mkDic(bits):
    dic = {}
    for i in bits:
        dic[i[0]]=i[2]
    return dic

def mapBits(dic,img):
    compressed=img.copy()
    row,col = compressed.shape
    for i in range(row):
        for j in range(col):
            compressed[i][j]=int(dic[img[i][j]])
    return compressed
    
#------------------------------------------------------------------------------------------
#                                        Lavg
#------------------------------------------------------------------------------------------
def getBitDepth(bits):
    bd = []
    for i in bits:
        bd.append((i[0],i[1],len(i[2])))
    return bd

def Lavg(bd):
    total = 0
    for i in bd:
        total += i[1]*i[2]
    return total
#------------------------------------------------------------------------------------------
#                               Convert Tuples to Strings
#------------------------------------------------------------------------------------------
def getStrings(keys):
    keyList = []
    for i in keys:
        entree = str(i)+':\t'+str(keys[i])
        keyList.append(entree)
    return keyList
        
#------------------------------------------------------------------------------------------
#                                        MAIN
#------------------------------------------------------------------------------------------
img = readImg()
# M,N = img.shape
# MN = M*N
freq = getFreq(img)
prk = getPrk(img,freq)
cs = corcoranStage(prk)
bits = getBits(cs)
keys = mkDic(bits)
compressed_img = mapBits(keys,img)
lavg = Lavg(getBitDepth(bits))
print('Lavg: ', lavg)
print('Compression Ratio: ', 8/lavg)
with open('keys.txt','w') as file:
    for line in getStrings(keys):
        file.write(str(line))
        file.write('\n')
cv2.imwrite("original.png",img)
cv2.imwrite('CorcoranCodingImage.png',compressed_img)
