'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Sunday August 18th 2019 5:52:52 pm
------------------------------------------------------
'''

# Assumptions: cv2.warpAffine allowed for this assignment. If not allowed, then uncomment lines [33-39] and [52-57].

import cv2
import numpy as np

Image = cv2.imread("cameramanimage_22843.tif")
cv2.imwrite("Original.png", Image)
# Image = cv2.imread("temp.png")
Output = np.zeros((Image.shape[0], Image.shape[1], 3), dtype=np.uint8)
Size = Image.shape

# U = np.asarray([[10, 15, 1],[8, 3, 1],[11, 17, 1]])
# U = np.asarray([[10, 15],[8, 3],[11, 17], [5, 11], [6, 13]])
U = np.asarray([[10, 15, 1],[8, 3, 1],[11, 17, 1], [5, 11, 1], [6, 13, 1]])

# V = np.asarray([[33, 20, 1], [18, 7, 1], [37, 22, 1]])
# V = np.asarray([[33, 20], [18, 7], [37, 22], [20, 13], [23, 16]])
V = np.asarray([[33, 20, 1], [18, 7, 1], [37, 22, 1], [20, 13, 1], [23, 16, 1]])

# print(np.matmul(np.linalg.inv(np.matmul(U.T, U)), U.T))
T = np.matmul(np.matmul(np.linalg.inv(np.matmul(U.T, U)), U.T), V)
print("Transformation Matrix")
print(T)

# To show mapping of the pixels.
# for i in range(Size[0]):
#     for j in range(Size[1]):
#         xyz = np.matmul(np.asarray([i, j, 1]), T)
#         for k in range(Size[2]):
#             if (int(xyz[0]) < Size[0] and int(xyz[0]) >= 0 and int(xyz[1]) < Size[1] and int(xyz[1]) >= 0):
#                 Output[int(xyz[0]), int(xyz[1]), k] = Image[i, j, k]


cv2.imwrite("TranformedImage2.jpg", Output)


# print(T[:, :2].T)
Output = cv2.warpAffine(Image, T[:, :2].T, (Size[0], Size[1]))
Output = cv2.resize(Output, Output.shape[:2], interpolation=cv2.INTER_CUBIC)
cv2.imwrite("TranformedImage.jpg", Output)

T = np.linalg.inv(T)

# for i in range(Size[0]):
#     for j in range(Size[1]):
#         xyz = np.matmul(np.asarray([i, j, 1]), T)
#         for k in range(Size[2]):
#             if (int(xyz[0]) < Size[0] and int(xyz[0]) >= 0 and int(xyz[1]) < Size[1] and int(xyz[1]) >= 0):
#                 Output[int(xyz[0]), int(xyz[1]), k] = Image[i, j, k]

Output2 = cv2.warpAffine(Output, T[:, :2].T, (Size[0], Size[1]))
Output2 = cv2.resize(Output2, Output2.shape[:2], interpolation=cv2.INTER_CUBIC)
cv2.imwrite("TranformedImage2.jpg", Output2)
