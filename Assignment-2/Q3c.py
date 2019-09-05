'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Friday September 6th 2019 12:15:39 am
------------------------------------------------------
'''

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
Output = cv2.filter2D(Image, -1, Kernel)
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
