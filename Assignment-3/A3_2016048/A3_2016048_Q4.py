'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Wednesday October 2nd 2019 7:44:23 pm
------------------------------------------------------
'''

# Question 4

import numpy as np
import cv2

W = np.ones((3, 3), dtype=np.float64)
W /= 9

I = cv2.imread("Q3_input.png", 0)

I = I.astype(np.float64)

I_cropped = I[:512, :512]
# cv2.imwrite("Q3_in.png", I_cropped)

I_Pad = np.zeros((514, 514), dtype=np.float64)
I_Pad[0:512, 0:512] = I_cropped[:, :]

W_Pad = np.zeros((514, 514), dtype=np.float64)
W_Pad[0:3, 0:3] = W[:, :]

I_fft = np.fft.fft2(I_Pad)
W_fft = np.fft.fft2(W_Pad)

# I_fft = np.fft.fftshift(I_fft)
# W_fft = np.fft.fftshift(W_fft)

H = np.multiply(W_fft, I_fft)

Sub = I_fft - H

Sub += I_fft

# Sub = np.fft.ifftshift(Sub)

Final = np.fft.ifft2(Sub)

Final = np.real(Final)

Final = Final[:512, :512]

cv2.imwrite("Q3_output.png", Final)



