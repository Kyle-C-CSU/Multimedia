import cv2
import copy
import numpy as np


#Create Python program that implements Huffman coding technique to reduce the enclosed image 
#file size (not the image dimenssion).
#Save the output file and the key codes.
#Compare the image file size before and after. 


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
def getPrk(img, freq:dict):
    m,n = img.shape
    MN = m*n
    prk = {}
    l1 = [(freq[i]/MN, i) for i in freq]
    l1.sort(reverse=True)
    for i in l1:
        prk[i[1]] = i[0]

    """
    for i in freq:
        prk[i] = float(freq[i]/MN)
    """
    return prk

#------------------------------------------------------------------------------------------
#                          Recursively Convert integer to Binary 
#------------------------------------------------------------------------------------------
def itob(i:int):
    if i == 0:
        return "0"
    return itob(i//2)+str(i%2)

#------------------------------------------------------------------------------------------
#                               Convert Binary to integer 
#------------------------------------------------------------------------------------------
def btoi(binary: str):
    if binary == "":
        return 0
    integer = 0
    size = len(binary)
    for i in binary:
        integer += int(binary[size - 1 - i])*pow(2,i)

#------------------------------------------------------------------------------------------
#                                   Recursively Do Huff 
#------------------------------------------------------------------------------------------
def recMadHuff(r:list):
    if len(r) == 2:
        return r
    pL = [r.pop(), r.pop()]
    r.append(pL[0] + pL[1])
    r.sort(reverse=True)
    return recMadHuff(copy.deepcopy(r))+pL

#------------------------------------------------------------------------------------------
#                                       Assign bits 
#------------------------------------------------------------------------------------------
def assBits(bits: list, vk: list):
    ans = dict()
    for i in bits:
        #print(i, vk[0])
        if vk and i[0] == vk[0][0]:
            ans[vk[0][1]] = i[1]
            vk.pop(0)
    return ans

#------------------------------------------------------------------------------------------
#                                       Map back to img
#------------------------------------------------------------------------------------------
def mapBack(img, ans:dict):
    #get row and col of gray scale 
    row,col = img.shape
    for i in range(row):
        for j in range(col):
            img[i][j] = ans[img[i][j]]

    return np.uint8(img)

#------------------------------------------------------------------------------------------
#                                        MAIN
#------------------------------------------------------------------------------------------
if __name__ == '__main__':
    img = readImg()
    freq = getFreq(img)
    prk = getPrk(img,freq) # sort by density not color since we use dens for huff
    r = list(prk.values())

    rec = recMadHuff(copy.deepcopy(r))
    rec.sort(reverse=True)
    if rec[0] != r[0]:
        s = rec[0]
        rec[0] = rec[1]
        rec[1] = rec[0]

    ans = []
    head = rec[0:2]
    head[0] = (head[0], "1")
    head[1] = (head[1], "")

    for enum, i in enumerate(rec[2:]):
        ans.append((i, itob(enum)))

    ans = head + ans

    vk = list(map(lambda x, y:(x,y), r, list(prk.keys())))

    ans = assBits(ans, vk)

    print(len(ans))

    f = open("demofile2.txt", "w")
    for i in ans:
        f.write(str(i)+" "+str(ans[i])+"\n")
    f.close()
    
    Lavg = 0
    for i in ans:
        Lavg += len(ans[i])*i
    Cr = 8/Lavg
    print("compression rate: ", Cr)

    cImg = mapBack(copy.deepcopy(img), ans)
    cv2.imshow("original",img)
    cv2.imshow("compress", cImg)
    cv2.waitKey(0)
    cv2.imwrite('compressQuiz2.png', cImg)