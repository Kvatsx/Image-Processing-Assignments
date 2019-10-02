'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Wednesday September 4th 2019 1:51:16 am
------------------------------------------------------
'''
# Assumption- If cv2.filter2D is not allowed then i would be allowed to use my own AVG filter, written in this file.
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

Image = cv2.imread("Chandrayaan2 - Q3a-inputimage.png", 0)
Image = Image.astype(float)
print("Image.shape", Image.shape)
Kernel = np.ones((7, 7), dtype=np.float32) / 49

def AvgFilter(Image, kSizeX, kSizeY):
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
                        num += Image[row, col]
            Result[i, j] = num/(kSizeX * kSizeY)
    return Result


BlurImage = cv2.filter2D(Image, -1, Kernel)
# BlurImage = AvgFilter(Image, 7, 7)
print("BlurImage.shape", BlurImage.shape)

# UnSharpMask = np.zeros((Image.shape), dtype=float)
# for i in range(Image.shape[0]):
#     for j in range(Image.shape[1]):
#         if ((Image[i, j] - BlurImage[i, j]) < 0):
#             UnSharpMask[i, j] = 0
#         else:
#             UnSharpMask[i, j] = Image[i, j] - BlurImage[i, j]                  
# print(UnSharpMask)

UnSharpMask = Image + Image - BlurImage

# Output = np.zeros((Image.shape), dtype=float)
# for i in range(Image.shape[0]):
#     for j in range(Image.shape[1]):
#         if ((Image[i, j] + UnSharpMask[i, j]) > 255):
#             Output[i, j] = 255
#         else:
#             Output[i, j] = Image[i, j] + UnSharpMask[i, j]

for i in range(Image.shape[0]):
    for j in range(Image.shape[1]):
        if (UnSharpMask[i, j] > 255):
            UnSharpMask[i, j] = 255
        if (UnSharpMask[i, j] < 0):
            UnSharpMask[i, j] = 0

# UnSharpMask = np.subtract(Image, BlurImage)

# Output = np.add(Image, UnSharpMask)

# Output = Output.astype(np.uint8)
Output = UnSharpMask.astype(np.uint8)
cv2.imwrite("Q3_Output.png", Output)
