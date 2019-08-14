'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Tuesday August 13th 2019 3:53:25 pm
------------------------------------------------------
'''

import numpy as np
import cv2
import math

Image = cv2.imread("cameramanimage_22843.tif")

Scale = 2
Output = np.zeros((Scale*Image.shape[0], Scale*Image.shape[1], Image.shape[2]), dtype=np.uint8)

for k in range(Output.shape[2]):
    for i in range(Output.shape[0]):
        for j in range(Output.shape[1]):
            x = math.floor(i/Scale)
            y = math.floor(j/Scale)
            Output[i, j, k] = Image[x, y, k]

cv2.imwrite("Original.png", Image)
cv2.imwrite("Interpolated.png", Output)

