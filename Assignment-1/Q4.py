'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Sunday August 18th 2019 5:52:52 pm
------------------------------------------------------
'''

import cv2
import numpy as np

Image = cv2.imread("cameramanimage_22843.tif")
Output = np.zeros((Image.shape), dtype=np.uint8)

TranformationMat = [
    [9/4, 7/8, -21/8],
    [-1/4, 9/8, 45/8],
    [0, 0, 1]
    ]

T = np.asarray(TranformationMat)


for i in range(Image.shape[0]):
    for j in range(Image.shape[1]):
        C = np.asarray([i, j, 1])
        NC = np.matmul(T, C)
        print(NC, NC.shape)
        for k in range(Image.shape[2]):
            Output[NC[0], NC[1], k] = Image[i, j, k]

cv2.imwrite("Original.png", Image)
cv2.imwrite("TranformedImage.png", Output)



