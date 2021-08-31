
import cv2
import numpy as np
x = 15
y = 8
filename = 'f:/vsc_workspace/opencv/0826/c_1.BMP'
filename2 =  'f:/vsc_workspace/opencv/0826/cp_1.BMP'
img1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
# ret, binary = cv2.threshold(gray, 50 ,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print("threshold value: %s" ,ret)
img1 = img1.astype(np.int32)
img2 = img2.astype(np.int32)

pmin = np.zeros(1280)
pmax = np.zeros(1280)
pmean = np.zeros(1280)

img3 = img2 - img1
rows, cols = img2.shape
for i in range(cols):
    pmin[i] = np.min(img2[: , i] - img1[: , i])
    pmax[i] = np.max(img2[: , i] - img1[: , i])
    pmean[i] =(pmin[i] + pmax[i])/2

img4 = img3*(-255 / (pmax-pmin)) + 255 + (255 + pmin)/(pmax-  pmin)
for i in range(rows):
    for j in range(cols):
        if img4[i,j] > 255:
            img4[i,j] = 255
cv2.imshow('i',img4.astype('uint8'))
cv2.waitKey(2000)