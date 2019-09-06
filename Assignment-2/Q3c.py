'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Friday September 6th 2019 12:15:39 am
------------------------------------------------------
'''
# Assumption- If cv2.filter2D is not allowed then i would be allowed to use my own AVG filter, written in this file.

import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

Image = cv2.imread("Chandrayaan2 - Q3a-inputimage.png", 0)
# Image = Image.astype(float)
print("Image.shape", Image.shape)
Kernel = np.ones((7, 7), dtype=np.float32) * -1
Kernel[3, 3] = 97
Kernel /= 49

def Filter(Image, kSizeX, kSizeY, Kernel):
    Result = np.zeros((Image.shape[0], Image.shape[1]))
    kCenterX = kSizeX//2
    kCenterY = kSizeY//2

    for i in range(Image.shape[0]):
        for j in range(Image.shape[1]):
            num = 0
            for k in range(kSizeX):
                for l in range(kSizeY):
                    row = i - kCenterX + k
                    col = j - kCenterY + l
                    # print(row, col)
                    if ( row >= 0 and row < Image.shape[0] and col >= 0 and col < Image.shape[1] ):
                        num += Image[row, col]*Kernel[k, l]
            Result[i, j] = num
    return Result

Output = cv2.filter2D(Image, -1, Kernel)
# Output = Filter(Image, 7, 7, Kernel)
cv2.imwrite("Output3c.png", Output)

Image2 = cv2.imread("Q3_Output.png", 0)
Image2 = Image2.astype(float)
Output = Output.astype(float)

Sub = Output - Image2
for i in range(Sub.shape[0]):
    for j in range(Sub.shape[1]):
        if (Sub[i, j] < 0):
            Sub[i, j] = abs(Sub[i, j])
        if (Sub[i, j] > 255):
            diff = Sub[i, j] - 255
            Sub[i, j] = 255 - diff

Sub = Sub.astype(np.uint8)
cv2.imwrite("Sub.png", Sub)
