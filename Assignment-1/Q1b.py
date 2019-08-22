'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
@Date: Wednesday August 21st 2019 4:28:58 pm
------------------------------------------------------
'''

import cv2
import numpy as np

R = [0, 1, 2, 3]
Pr = [0.4, 0.2, 0, 0.4]
BitDept = 2

CDF = [Pr[0]]
for i in range(1, len(Pr)):
    CDF.append(CDF[i-1] + Pr[i])

L = pow(2, BitDept)
print("L", L)
print("CDF:", CDF)

S = [0 for i in range(len(R))]

for i in range(len(R)):
    S[i] = round((L-1)*CDF[i])

PS = [0 for i in range(len(R))]
for i in range(len(R)):
    PS[S[i]] += Pr[R[i]]

print("R", "  ", "S", " ", "P(s)")
for i in range(len(R)):
    print(R[i], "->", S[i], "->", PS[S[i]])

