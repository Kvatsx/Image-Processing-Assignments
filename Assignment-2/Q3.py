'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Wednesday September 4th 2019 1:51:16 am
------------------------------------------------------
'''

import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

Image = cv2.imread("Chandrayaan2 - Q3a-inputimage.png", 0)
Image = Image.astype(float)
print("Image.shape", Image.shape)
Kernel = np.ones((7, 7), dtype=np.float32) / 49
BlurImage = cv2.filter2D(Image, -1, Kernel)
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
