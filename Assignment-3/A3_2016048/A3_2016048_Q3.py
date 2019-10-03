'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Tuesday October 1st 2019 10:03:42 pm
------------------------------------------------------
'''

# Question 3

import numpy as np
import cv2

def rot(W):
    W_New = np.zeros((5, 5), dtype=np.float64)
    cx = 1
    cy = 1
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            x = i-cx
            y = j-cy
            W_New[x%(5), y%(5)] = W[i, j]
    return W_New

def inv_rot(W):
    W_New = np.zeros((5, 5), dtype=np.float64)
    cx = 1
    cy = 1
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            x = i+cx
            y = j+cy
            W_New[x%(5), y%(5)] = W[i, j]
    return W_New

I = np.asarray([
    [1, 3, 4],
    [2, 5, 3],
    [6, 8, 9]
], dtype=np.float64)

W = np.asarray([
    [-1, -2, -3],
    [-4, 0, 1],
    [-6, -5, -1]
], dtype=np.float64)


I_Pad = np.zeros((5, 5), dtype=np.float64)

I_Pad[:3, :3] = I[:, :]
W_Pad = rot(W)
print(W_Pad)
print()

I_fft = np.fft.fft2(I_Pad)
W_fft = np.fft.fft2(W_Pad)

# I_fft = np.fft.fftshift(I_fft)
# W_fft = np.fft.fftshift(W_fft)

H = np.multiply(I_fft, W_fft)

# H = np.fft.ifftshift(H)

Final = np.fft.ifft2(H)

Final = np.real(Final)
print(Final)
print()

Final = inv_rot(Final)
print(Final)

