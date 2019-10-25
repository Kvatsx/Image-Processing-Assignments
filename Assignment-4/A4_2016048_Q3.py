'''
------------------------------------------------------
@Author: Kaustav Vats (kaustav16048@iiitd.ac.in)
@Roll-No: 2016048
------------------------------------------------------
'''

import cv2
import numpy as np
from math import sqrt

def addGNoise(Image, mean, var):
    Gauss = np.random.normal(mean, sqrt(var), Image.shape)
    G = Image + Gauss
    return G

def LocalVar(G, x, y, GridSize):
    kCenterX = GridSize//2
    kCenterY = GridSize//2
    Arr = []
    for k in range(GridSize):
        for l in range(GridSize):
            row = x - kCenterX + k
            col = y - kCenterY + l
            if ( row >= 0 and row < G.shape[0] and col >= 0 and col < G.shape[1] ):
                Arr.append(G[row, col])
            else:
                Arr.append(0)
    Arr = np.asarray(Arr)
    return np.mean(Arr), np.var(Arr)

def AdaptiveFiltering(G, nVar, GridSize):
    Result = np.zeros((G.shape[0], G.shape[1]), dtype=np.uint8)
    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            lMean, lVar = LocalVar(G, i, j, GridSize)

            if (nVar == 0):
                Result[i, j] = G[i, j]
            elif (nVar >= lVar):
                Result[i, j] = lMean
            else:
                Result[i, j] = G[i, j] - (nVar/lVar) * (G[i, j] - lMean)
    return Result


if __name__ == "__main__":

    Image = cv2.imread("image_2.png", 0)
    variance = 49
    GridSize = 5

    G = addGNoise(Image, 0, variance)
    cv2.imwrite("NoisyImg.png", G)

    Result = AdaptiveFiltering(G, variance, GridSize)
    cv2.imwrite("Result.png", Result)
