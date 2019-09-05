'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Tuesday September 3rd 2019 3:14:33 pm
------------------------------------------------------
'''

import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

Image = cv2.imread("Q2-input image.tif", 0)
cv2.imwrite("Original.png", Image)
# H1 = cv2.calcHist([Image],[0], None, [256], [0,256])
H1 = np.zeros(256)
H2 = np.zeros(256)
Image2 = np.random.randint(0, 256, (Image.shape[0], Image.shape[1]))
for i in range(Image.shape[0]):
    for j in range(Image.shape[1]):
        H1[Image[i, j]] += 1
        H2[Image2[i, j]] += 1


plt.figure(1)

plt.subplot(221)
# plt.bar(np.arange(256), H1, color='r')
# plt.title('Original Image Histogram')
# plt.xlabel("Pixel value")
# plt.ylabel("Frequency")
plt.title("Original Image")
plt.imshow(Image)


plt.subplot(222)
plt.bar(np.arange(256), H2, color='b')
plt.title('Specified Histogram')
plt.xlabel("Pixel value")
plt.ylabel("Frequency")

# print(H2)

ProbH1 = H1/(Image.shape[0]*Image.shape[1])
ProbH2 = H2/(Image.shape[0]*Image.shape[1])
# print(ProbH2)

CDFH1 = ProbH1
CDFH2 = ProbH2
for i in range(1, 256):
    CDFH1[i] += CDFH1[i-1]
    CDFH2[i] += CDFH2[i-1]

CDFH1 = CDFH1 * 255
CDFH2 = CDFH2 * 255

CDFH1 = np.around(CDFH1, decimals=0)
CDFH2 = np.around(CDFH2, decimals=0)

# print(CDFH1)
# print(CDFH2)

Mapping = np.zeros(256, dtype=np.int64)
for i in range(256):
    for j in range(256):
        if (CDFH2[j] >= CDFH1[i]):
            Mapping[i] = j
            break
print("Mapping\n", Mapping)

H3 = np.zeros(256, dtype=np.int)
for i in range(Image.shape[0]):
    for j in range(Image.shape[1]):
        Image[i, j] = Mapping[Image[i, j]]
        H3[Image[i, j]] += 1

cv2.imwrite("Output.png", Image)

plt.subplot(223)
plt.bar(np.arange(256), H3, color='g')
plt.title('Matched Image Histogram')
plt.xlabel("Pixel value")
plt.ylabel("Frequency")

plt.subplot(224)
plt.title("Macthed Image")
plt.imshow(Image)

plt.show()