import cv2
from matplotlib import pyplot as plt
import numpy as np

imagen = cv2.imread('imagen sencilla.jpg')

matriz_img=np.asarray(imagen)
print(matriz_img.shape)
print(imagen)

#HSV
img_hsv = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV', img_hsv)
print('\nValores HSV')
print(img_hsv)

#LAB
img_lab = cv2.cvtColor(imagen,cv2.COLOR_BGR2LAB)
#cv2.imshow('HSV', img_hsv)
print('\nValores LAB')
print(img_lab)
