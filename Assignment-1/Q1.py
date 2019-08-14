'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Tuesday August 13th 2019 2:42:08 pm
------------------------------------------------------
'''

import numpy as np
import cv2
import math

Image = np.zeros((2, 2), dtype=np.uint8)
Image[0, 0] = 1
Image[0, 1] = 2
Image[1, 0] = 4
Image[1, 1] = 5

Sx = 2
Sy = 1

Output = np.zeros((Sy*Image.shape[0], Sx*Image.shape[1]), dtype=np.uint8)

for i in range(Output.shape[0]):
    for j in range(Output.shape[1]):
        x = math.floor(i/Sy)
        y = math.floor(j/Sx)
        Output[i, j] = Image[x, y]

print("Input Image...")
for i in range(Image.shape[0]):
    for j in range(Image.shape[1]):
        print(Image[i, j], end=' ')
    print()

print("Interpolated Image...")
for i in range(Output.shape[0]):
    for j in range(Output.shape[1]):
        print(Output[i, j], end=' ')
    print()


